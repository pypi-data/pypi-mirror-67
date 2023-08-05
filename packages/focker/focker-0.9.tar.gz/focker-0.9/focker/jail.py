#
# Copyright (C) Stanislaw Adaszewski, 2020
# License: GNU General Public License v3.0
# URL: https://github.com/sadaszewski/focker
# URL: https://adared.ch/focker
#

import subprocess
from .zfs import *
import random
import shutil
import json
from tabulate import tabulate
import os
import jailconf
from .mount import getmntinfo
import shlex
# import pdb


def jail_fs_create(image=None):
    sha256 = bytes([ random.randint(0, 255) for _ in range(32) ]).hex()
    lst = zfs_list(fields=['focker:sha256'], focker_type='image')
    lst = list(filter(lambda a: a[0] == sha256, lst))
    if lst:
        raise ValueError('Whew, a collision...')
    poolname = zfs_poolname()
    for pre in range(7, 32):
        name = poolname + '/focker/jails/' + sha256[:pre]
        if not zfs_exists(name):
            break
    if image:
        image, _ = zfs_find(image, focker_type='image', zfs_type='snapshot')
        zfs_parse_output(['zfs', 'clone', '-o', 'focker:sha256=' + sha256, image, name])
    else:
        print('Creating empty jail:', name)
        zfs_parse_output(['zfs', 'create', '-o', 'focker:sha256=' + sha256, name])
    return name


def gen_env_command(command, env):
    if any(map(lambda a: ' ' in a, env.keys())):
        raise ValueError('Environment variable names cannot contain spaces')
    env = [ 'export ' + k + '=' + shlex.quote(v) \
        for (k, v) in env.items() ]
    command = ' && '.join(env + [ command ])
    return command


def quote(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('\'', '\\\'')
    s = '\'' + s + '\''
    return s


def jail_create(path, command, env, mounts, hostname=None, overrides={}):
    name = os.path.split(path)[-1]
    if os.path.exists('/etc/jail.conf'):
        conf = jailconf.load('/etc/jail.conf')
    else:
        conf = jailconf.JailConf()
    conf[name] = blk = jailconf.JailBlock()
    blk['path'] = path
    if command:
        command = gen_env_command(command, env)
        command = quote(command)
        print('command:', command)
        blk['exec.start'] = command
    prestart = [ 'cp /etc/resolv.conf ' +
        shlex.quote(os.path.join(path, 'etc/resolv.conf')) ]
    poststop = []
    if mounts:
        for (from_, on) in mounts:
            if not from_.startswith('/'):
                from_, _ = zfs_find(from_, focker_type='volume')
                from_ = zfs_mountpoint(from_)
            prestart.append('mount -t nullfs ' + shlex.quote(from_) +
                ' ' + shlex.quote(os.path.join(path, on.strip('/'))))
        poststop += [ 'umount -f ' +
            os.path.join(path, on.strip('/')) \
            for (_, on) in reversed(mounts) ]
    if prestart:
        blk['exec.prestart'] = quote(' && '.join(prestart))
    if poststop:
        blk['exec.poststop'] = quote(' && '.join(poststop))
    blk['persist'] = True
    blk['interface'] = 'lo1'
    blk['ip4.addr'] = '127.0.1.0'
    blk['mount.devfs'] = True
    blk['exec.clean'] = True
    blk['host.hostname'] = hostname or name
    for (k, v) in overrides.items():
        blk[k] = quote(v)
    conf.write('/etc/jail.conf')
    return name


def get_jid(path):
    data = json.loads(subprocess.check_output(['jls', '--libxo=json']))
    lst = data['jail-information']['jail']
    lst = list(filter(lambda a: a['path'] == path, lst))
    if len(lst) == 0:
        raise ValueError('JID not found for path: ' + path)
    if len(lst) > 1:
        raise ValueError('Ambiguous JID for path: ' + path)
    return str(lst[0]['jid'])


def do_mounts(path, mounts):
    print('mounts:', mounts)
    for (source, target) in mounts:
        if source.startswith('/'):
            name = source
        else:
            name, _ = zfs_find(source, focker_type='volume')
            name = zfs_mountpoint(name)
        while target.startswith('/'):
            target = target[1:]
        subprocess.check_output(['mount', '-t', 'nullfs',
            shlex.quote(name), shlex.quote(os.path.join(path, target))])


def undo_mounts(path, mounts):
    for (_, target) in reversed(mounts):
        while target.startswith('/'):
            target = target[1:]
        subprocess.check_output(['umount', '-f',
            shlex.quote(os.path.join(path, target))])


def jail_run(path, command, mounts=[]):
    command = ['jail', '-c', 'host.hostname=' + os.path.split(path)[1], 'persist=1', 'mount.devfs=1', 'interface=lo1', 'ip4.addr=127.0.1.0', 'path=' + path, 'command', '/bin/sh', '-c', command]
    print('Running:', ' '.join(command))
    try:
        do_mounts(path, mounts)
        shutil.copyfile('/etc/resolv.conf', os.path.join(path, 'etc/resolv.conf'))
        res = subprocess.run(command)
    finally:
        try:
            subprocess.run(['jail', '-r', get_jid(path)])
        except ValueError:
            pass
        subprocess.run(['umount', '-f', os.path.join(path, 'dev')])
        undo_mounts(path, mounts)
    if res.returncode != 0:
        # subprocess.run(['umount', os.path.join(path, 'dev')])
        raise RuntimeError('Command failed')


def jail_stop(path):
    try:
        jid = get_jid(path)
        jailname = os.path.split(path)[-1]
        subprocess.run(['jail', '-r', jailname])
    except ValueError:
        print('JID could not be determined')
    # import time
    # time.sleep(1)
    mi = getmntinfo()
    for m in mi:
        mntonname = m['f_mntonname'].decode('utf-8')
        if mntonname.startswith(path + os.path.sep):
            print('Unmounting:', mntonname)
            subprocess.run(['umount', '-f', mntonname])


def jail_remove(path):
    print('Removing jail:', path)
    jail_stop(path)
    subprocess.run(['zfs', 'destroy', '-r', '-f', zfs_name(path)])
    if os.path.exists('/etc/jail.conf'):
        conf = jailconf.load('/etc/jail.conf')
        name = os.path.split(path)[-1]
        if name in conf:
            del conf[name]
            conf.write('/etc/jail.conf')


def command_jail_create(args):
    name = jail_fs_create(args.image)
    if args.tags:
        zfs_tag(name, args.tags)
    path = zfs_mountpoint(name)
    jail_create(path, args.command,
        { a.split(':')[0]: ':'.join(a.split(':')[1:]) \
            for a in args.env },
        [ [a.split(':')[0], ':'.join(a.split(':')[1:])] \
            for a in args.mounts ],
        args.hostname )
    print(sha256)
    print(path)


def command_jail_start(args):
    name, _ = zfs_find(args.reference, focker_type='jail')
    path = zfs_mountpoint(name)
    jailname = os.path.split(path)[-1]
    subprocess.run(['jail', '-c', jailname])


def command_jail_stop(args):
    name, _ = zfs_find(args.reference, focker_type='jail')
    path = zfs_mountpoint(name)
    jail_stop(path)


def command_jail_remove(args):
    name, _ = zfs_find(args.reference, focker_type='jail')
    path = zfs_mountpoint(name)
    jail_remove(path)


def command_jail_exec(args):
    name, _ = zfs_find(args.reference, focker_type='jail')
    path = zfs_mountpoint(name)
    jid = get_jid(path)
    subprocess.run(['jexec', str(jid)] + args.command)


def jail_oneshot(image, command, env, mounts):
    # pdb.set_trace()
    name = jail_fs_create(image)
    path = zfs_mountpoint(name)
    jailname = jail_create(path,
        ' '.join(map(shlex.quote, command or ['/bin/sh'])),
        env, mounts)
    subprocess.run(['jail', '-c', jailname])
    jail_remove(path)


def command_jail_oneshot(args):
    env = { a.split(':')[0]: ':'.join(a.split(':')[1:]) \
        for a in args.env }
    mounts = [ [ a.split(':')[0], a.split(':')[1] ] \
        for a in args.mounts]
    jail_oneshot(args.image, args.command, env, mounts)


# Deprecated
def command_jail_oneshot_old():
    base, _ = zfs_snapshot_by_tag_or_sha256(args.image)
    # root = '/'.join(base.split('/')[:-1])
    for _ in range(10**6):
        sha256 = bytes([ random.randint(0, 255) for _ in range(32) ]).hex()
        name = sha256[:7]
        name = base.split('/')[0] + '/focker/jails/' + name
        if not zfs_exists(name):
            break
    zfs_run(['zfs', 'clone', '-o', 'focker:sha256=' + sha256, base, name])
    try:
        mounts = list(map(lambda a: a.split(':'), args.mounts))
        jail_run(zfs_mountpoint(name), args.command, mounts)
        # subprocess.check_output(['jail', '-c', 'interface=lo1', 'ip4.addr=127.0.1.0', 'path=' + zfs_mountpoint(name), 'command', command])
    finally:
        # subprocess.run(['umount', zfs_mountpoint(name) + '/dev'])
        zfs_run(['zfs', 'destroy', '-f', name])
        # raise

def command_jail_list(args):
    lst = zfs_list(fields=['focker:sha256,focker:tags,mountpoint'], focker_type='jail')
    jails = subprocess.check_output(['jls', '--libxo=json'])
    jails = json.loads(jails)['jail-information']['jail']
    jails = { j['path']: j for j in jails }
    lst = list(map(lambda a: [ a[1],
        a[0] if args.full_sha256 else a[0][:7],
        a[2],
        jails[a[2]]['jid'] if a[2] in jails else '-' ], lst))
    print(tabulate(lst, headers=['Tags', 'SHA256', 'mountpoint', 'JID']))


def command_jail_tag(args):
    name, _ = zfs_find(args.reference, focker_type='jail')
    zfs_untag(args.tags, focker_type='jail')
    zfs_tag(name, args.tags)


def command_jail_untag(args):
    zfs_untag(args.tags, focker_type='jail')


def command_jail_prune(args):
    jails = subprocess.check_output(['jls', '--libxo=json'])
    jails = json.loads(jails)['jail-information']['jail']
    used = set()
    for j in jails:
        used.add(j['path'])
    lst = zfs_list(fields=['focker:sha256,focker:tags,mountpoint,name'], focker_type='jail')
    for j in lst:
        if j[1] == '-' and (j[2] not in used or args.force):
            jail_remove(j[2])

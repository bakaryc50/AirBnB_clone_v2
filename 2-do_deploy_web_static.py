#!/usr/bin/python3
"""
Deploy archive to my webserver
"""
from os.path import isfile, join, basename, sep, splitext
from shlex import quote
from time import strftime
from fabric.api import local, env, put, run


env.hosts = ["34.139.62.54", "34.74.103.174"]


def do_pack():
    """ Archive the contents of web_static before sending
    """
    now = strftime("%Y%m%d%H%M%S")
    tgz = join("versions", "web_static_{}.tgz".format(now))

    local("mkdir -p versions")
    local("tar -czf {} web_static".format(quote(tgz)))

    if isfile(tgz):
        return tgz
    else:
        None


def do_deploy(archive_path):
    """ Deploy an archive to my web servers
    """
    if isfile(archive_path):
        source_name = basename(archive_path)
        source_path = join(sep, "tmp", source_name)
        dest_name = splitext(source_name)[0]
        dest_path = join(sep, "data", "web_static", "releases", dest_name)
        put(archive_path, source_path)
        run("mkdir -p {}".format(
            quote(dest_path)
        ))
        run("tar -xzf {} -C {}".format(
            quote(source_path),
            quote(dest_path)
        ))
        run("rm -f {}".format(
            quote(source_path)
        ))
        run("mv {} {}".format(
            join(quote(join(dest_path, "web_static")), "*"),
            quote(join(dest_path, ""))
        ))
        run("rm -rf {}".format(
            quote(join(dest_path, "web_static"))
        ))
        run("rm -rf {}".format(
            quote(join(sep, "data", "web_static", "current"))
        ))
        run("ln -s {} {}".format(
            quote(dest_path),
            quote(join(sep, "data", "web_static", "current"))
        ))
        return True
    return False

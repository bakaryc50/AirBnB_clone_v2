#!/usr/bin/python3
"""
Compress before sending
Generates a .tgz archive from the contents of the web_static folder
"""
from os.path import isfile, join
from shlex import quote
from time import strftime
from fabric.api import local


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

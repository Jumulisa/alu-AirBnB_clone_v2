#!/usr/bin/python3
<<<<<<< HEAD
"""
<<<<<<< HEAD
    Fabric script that generates a .tgz archive from the
    contents of the web_static folder of the AirBnB Clone repo.
"""
from os import makedirs
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Function that generates the archive. """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path

    except:
        return None
=======
    script that generates '.tgz' archive from the contents of the 'web_static'
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        function to compress directory into .tgz archive
        Return: Success - '.tgz' archive path
                Failure - None
    """
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b
=======
"""Fabric script which generates a tgz archive"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """TGZ"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
>>>>>>> eb430b99251ce235cda3c54a38c556ed236b6243

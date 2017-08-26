#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['66.70.184.24', '52.90.139.75']


def do_deploy(archive_path):
    """ deploy """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_file = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases" + new_file.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_file, new_folder))
        run("sudo rm /tmp/{}".format(new_file))
        run("sudo mv {}/web_static/* {}".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except Exception as e:
        print(e)
        return False

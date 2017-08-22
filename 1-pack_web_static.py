#!/usr/bin/python3
"""
fabric api
"""
from fabric.api import *
import time


def do_pack():
    """
    generates tgz file from contents of web_static
    """
    # strftime format: <year><month><day><hour><minute><second>
    current_time = time.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(current_time))
        return ("versions/web_static_{}.tgz".format(current_time))
    except:
        return (None)

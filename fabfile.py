# -*- coding: utf-8 -*-

import sys
import os
import re
import codecs
import sys
import pprint
import logging

from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists
from fabric.contrib.console import confirm

logging_level = logging.INFO

if os.environ.has_key('DEBUG'):
    logging_level = logging.DEBUG

logging.basicConfig(level=logging_level)

assert 'FABRIC_REMOTE_HOST' in os.environ
assert 'FABRIC_REMOTE_PATH' in os.environ
assert 'FABRIC_REMOTE_PASSWORD' in os.environ
assert 'PROJECT_VERSION' in os.environ

FABRIC_REMOTE_HOST = os.environ.get('FABRIC_REMOTE_HOST')
FABRIC_REMOTE_PATH = os.environ.get('FABRIC_REMOTE_PATH')
FABRIC_REMOTE_PASSWORD = os.environ.get('FABRIC_REMOTE_PASSWORD')

env.user = "root"
env.hosts = [FABRIC_REMOTE_HOST]
env.disable_known_hosts = True  
env.reject_unknown_hosts = False
env.use_ssh_config = False
env.password = FABRIC_REMOTE_PASSWORD

env.project = 'mongrey'
env.project_version = os.environ.get('PROJECT_VERSION', None)

env.project_base_path = FABRIC_REMOTE_PATH #"%s/%s" % (FABRIC_REMOTE_PATH, env.project)
env.project_path = "%s/%s" % (env.project_base_path, env.project_version)
env.project_path_latest = "%s/latest" % env.project_base_path
env.project_nginx_user = "root:nobody"

def test_remote():
    run('hostname')
    
def upload():
    
    if not env.project_version:
        abort("Not project version")

    print "-----------------------------------------------"        
    print "PROJECT VERSION : %s" % env.project_version
    print "-----------------------------------------------"
    
    if exists(env.project_path):
        abort("already binaries for this version [%s]" % env.project_version)        
    
    run('mkdir -vp %s' % env.project_path)
    
    """
    mongrey-migration
    mongrey-server
    mongrey-web

    mongrey-server-mongo
    mongrey-server-mysql
    mongrey-server-postgresql
    mongrey-server-sqlite

    mongrey-web-mongo
    mongrey-web-mysql
    mongrey-web-postgresql
    mongrey-web-sqlite
    """
    #`pwd`:/code
    with lcd('/code/dist'):
        put("mongrey*", env.project_path, mode=0644)

    with cd(env.project_base_path):
        run("rm -vf latest")
        run("ln -sf %s latest" % env.project_version)
        run("chown -R %s %s latest" % (env.project_nginx_user, env.project_version))
        run('find %s -type f' % env.project_base_path)
        
    

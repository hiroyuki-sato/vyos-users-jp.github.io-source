from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
env.publish_path = 'publish'
PUBLISH_PATH = env.publish_path

# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
#env.cloudfiles_username = 'my_rackspace_username'
#env.cloudfiles_api_key = 'my_rackspace_api_key'
#env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))
    if os.path.isdir(PUBLISH_PATH):
        local('rm -rf {publish_path}'.format(**env))

#def build():
#    local('pelican content -s pelicanconf.py')

#def rebuild():
#    clean()
#    build()

#def regenerate():
#    local('pelican content -r -s pelicanconf.py')

def serve():
    preview()
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

#def reserve():
#    preview()
#    serve()

def preview():
    clean()
    local('pelican content -s publishconf.py')

#def cf_upload():
#    rebuild()
#    local('cd {deploy_path} && '
#          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#          '-U {cloudfiles_username} '
#          '-K {cloudfiles_api_key} '
#          'upload -c {cloudfiles_container} .'.format(**env))

#@hosts(production)
#def publish():
#    local('pelican content -s publishconf.py')
#    project.rsync_project(
#        remote_dir=dest_path,
#        exclude=".DS_Store",
#        local_dir=DEPLOY_PATH.rstrip('/') + '/',
#        delete=True
#    )

def deploy():
    clean()
    local('pelican content -s publishconf.py')
    local('git clone git@github.com:vyos-users-jp/vyos-users-jp.github.io.git publish')
    local('cd {publish_path} && git pull'.format(**env))
    for f in os.listdir(PUBLISH_PATH):
        if os.path.isfile(f):
            os.remove(f)
    local('cp -pr {deploy_path}/. {publish_path}/'.format(**env))
    local('cd {publish_path} && git add -A'.format(**env))
    env.message = "Site updated"
    local('cd {publish_path} && git commit -m \"{message}\"'.format(**env))
    local('cd {publish_path} && git push origin master'.format(**env))

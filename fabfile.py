from fabric.api import *
import os

env.hosts = ['survey.firebelly.co']
env.user = 'firebelly'
env.remotepath = '/home/firebelly/webapps/pp-survey'
env.git_branch = 'master'
env.warn_only = True

def deploy(assets='y'):
  # build and sync production assets
  if assets != 'n':
    local('rm -rf web/assets/dist')
    local('yarn build:production')
    run('mkdir -p ' + env.remotepath + '/web/assets/dist')
    put('dist', env.remotepath + '/dist/')

def update():
  with cd(env.remotepath):
    run('git pull origin {0}'.format(env.git_branch))

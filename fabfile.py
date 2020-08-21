from fabric.api import *
import os

env.hosts = ['survey.firebelly.co']
env.user = 'firebelly'
env.remotepath = '/home/firebelly/webapps/pp_survey'
env.git_branch = 'master'
env.warn_only = True

def deploy(composer='y', assets='y'):
  update()
  if composer == 'y':
    composer_install()
  # build and sync production assets
  if assets != 'n':
    local('rm -rf web/assets/dist')
    local('yarn build:production')
    run('mkdir -p ' + env.remotepath + '/web/assets/dist')
    put('web/assets/dist', env.remotepath + '/web/assets/')
  with cd(env.remotepath):
    run('./craft clear-caches/compiled-templates')
    run('./craft invalidate-tags/template')
    run('./craft project-config/apply')

def update():
  with cd(env.remotepath):
    run('git pull origin {0}'.format(env.git_branch))

def composer_install():
  with cd(env.remotepath):
    run('~/bin/composer install')

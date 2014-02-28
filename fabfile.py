from fabric.api import env, run, sudo, local, settings
from fabric.context_managers import cd, prefix
#from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts, local
from fabric.decorators import roles
from fabric.contrib import project, files
import re

######## CHANGE BELOW TO SUIT YOUR PROJECT #######

env.deploy_user = "aes_local"
env.home_dir = "/var/www/vhosts/" + env.deploy_user + "/"
env.houston_version = 'v1.0.2'

env.git_repo = "git@bitbucket.org:powellc/adamsschool_com.git"
env.host = "adamsschool.com"
env.local_host = "11.0.0.100"
env.dbdump_file = 'aes_production-nightly.sql'

######### DO NOT EDIT BELOW THIS LINE ############

def provision():
    # Before we can vagrant up, we just need to grab a prod copy of the DB
    with settings(warn_only=True):
        local('scp powellc@%s:/var/backups/databases/latest/%s.bz2 .' % (env.host, env.dbdump_file))
        local('bunzip2 %s.bz2' % env.dbdump_file)

    with settings(warn_only=True):
        local('vagrant up')
        local('vagrant provision')

    # Clean up our DB files
    with settings(warn_only=True):
        local('rm %s.bz2' % env.dbdump_file)
        local('rm %s' % env.dbdump_file)

def get_media():
    # Just need to rsync the public media from production to local
    pass

def start():
    local('node ansible/proxy.js &')
    local('vagrant up')

def v():
    """Use Vagrant for testing"""
    env.user = 'vagrant'
    env.hosts = [env.local_host]   # Update the Vagrantinit file if you change this

    # retrieve the IdentityFile:
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = re.sub(r'^"|"$', '', result.split()[1])  # parse IdentityFile

def ve(command):
    with cd(env.home_dir + 'code/'):
        sudo("source %svenv/bin/activate" % env.home_dir + " && " + command, user=env.deploy_user)

def collect():
    """
    Run collect static.
    """
    with cd(env.home_dir + 'code/'):
        ve('python manage.py collectstatic --noinput')

def manage(cmd="", extra=""):
    '''
    Run a django management command
    '''
    with cd(env.home_dir + 'code/'):
        ve('python manage.py {0} {1}'.format(cmd, extra))

def reqs(cmd="", extra=""):
    '''
    Re install requirements.txt file
    '''
    with cd(env.home_dir + 'code/'):
        ve('pip install -r etc/requirements.txt')

def log():
    """
    View our logs
    """
    with cd(env.home_dir):
        sudo('tail -n 30 logs/supervisord.log')

def hup():
    '''
    HUP gunicorn
    '''
    sudo("supervisorctl restart %s" % env.deploy_user)

def test(apps=''):
    '''
    Test our django app
    '''
    with cd(env.home_dir + 'code/'):
        ve('python manage.py test %s' % apps) 

def free():
    """Check free memory."""
    run('free -m')

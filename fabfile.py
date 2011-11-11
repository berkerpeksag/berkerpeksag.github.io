from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts
from fabric.contrib import project, files

env.project_name = 'berkerpeksag'
env.root = '~/berkerpeksag'


def deploy():
    with cd(env.root):
        sudo('git pull')
        put('conf/gunicorn.conf', '/etc/init/%(project_name)s.conf' %
                                  env, use_sudo=True)
        sudo('initctl reload-configuration')


def start():
    """Start the Gunicorn process"""
    sudo('start %(project_name)s' % env)


def stop():
    """Stop the Gunicorn process"""
    sudo('stop %(project_name)s' % env)


def reload():
    """Reload the Gunicorn configuration"""
    sudo('reload %(project_name)s' % env)


def restart():
    """Restart the Gunicorn process"""
    stop_gunicorn()
    start_gunicorn()


def status():
    """Status of Gunicorn"""
    sudo('status %(project_name)s' % env)


def update_dependencies():
    """Update requirements remotely."""
    put('requirements.txt', '%(root)s/requirements.txt' % env, use_sudo=True)
    sudo('%(root)s/bin/pip install -r %(root)s/requirements.txt' % env)


def setup():
    sudo('virtualenv --no-site-packages %(project_name)s' % env)

    with cd(env.root):
        sudo('source bin/activate')
        sudo('git clone git://github.com/berkerpeksag/berkerpeksag.git .')

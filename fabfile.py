from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts
from fabric.contrib import project, files

env.project_name = 'berkerpeksag'
env.root = '~/'


def deploy():
    with cd('%(root)s%(project_name)s' % env):
        run('git pull')
        put('conf/gunicorn.conf', '/etc/init/%(project_name)s.conf' %
                                  env, use_sudo=True)
        run('initctl reload-configuration')


def start():
    """Start the Gunicorn process"""
    run('start %(project_name)s' % env)


def stop():
    """Stop the Gunicorn process"""
    run('stop %(project_name)s' % env)


def reload():
    """Reload the Gunicorn configuration"""
    run('reload %(project_name)s' % env)


def restart():
    """Restart the Gunicorn process"""
    stop_gunicorn()
    start_gunicorn()


def status():
    """Status of Gunicorn"""
    run('status %(project_name)s' % env)


def update_dependencies():
    """Update requirements remotely."""
    put('requirements.txt', '%(root)s/requirements.txt' % env, use_sudo=True)
    run('%(root)s/bin/pip install -r %(root)s/requirements.txt' % env)


def configure():
    with cd(env.root):
        run('git clone git://github.com/berkerpeksag/berkerpeksag.git')

    with cd('%(root)s%(project_name)s' % env):
        run('virtualenv --no-site-packages .')
        run('source bin/activate')
        put('conf/gunicorn.conf', '/etc/init/%(project_name)s.conf' % env)


def setup():
    pass


def hello():
    print 'World'

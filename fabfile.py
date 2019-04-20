# coding: utf-8

from contextlib import contextmanager

from fabric.api import cd, get, local, put, run, sudo, prefix

try:
    from fabenv import env
except ImportError:
    class ImproperlyConfigured(Exception):
        """Application is somehow improperly configured."""

    msg = "Kurulum için lütfen README.md belgesini okuyun."
    raise ImproperlyConfigured(msg)


@contextmanager
def venv():
    with cd('%(root)s%(project_name)s' % env):
        yield


def deploy():
    """Deploy the latest version."""
    with venv():
        run('git pull')

    restart_nginx()


def restart_nginx():
    """Restart the nginx process."""
    sudo('/etc/init.d/nginx restart')


def static():
    """Update static files."""
    with venv():
        sudo('rm -r static/')
        run('source bin/activate')
        sudo('python manage.py collectstatic --noinput')



def configure():
    """Configure basic tools."""
    with cd(env.root):
        run('git clone git://github.com/berkerpeksag/berkerpeksag.git')
        run('virtualenv venv')
        run('source venv/bin/activate')

    with venv():
        run('pip install -r requirements.txt')
        static()
        sudo('ln -s /home/wakefield/berkerpeksag/conf/nginx.conf /etc/nginx/sites-enabled/berkerpeksag.com')
        run('echo_supervisord_conf > supervisord.conf')
        sudo('mv supervisord.conf /etc/supervisord.conf')
        sudo('cat conf/supervisor.conf >> /etc/supervisord.conf')
        run('supervisord')

    restart_nginx()


def setup():
    """Setup the VM."""
    sudo('apt-get update && apt-get upgrade && apt-get install git-core sqlite3 '
         'python-sqlite python-setuptools python-pip python-dev build-essential '
         'nginx curl libcurl3')
    sudo('pip install virtualenv fabric')


def clean():
    """Clean the current setup."""
    stop()
    sudo('unlink /tmp/supervisor.sock')

    with cd(env.root):
        sudo('rm -r berkerpeksag/')
        sudo('rm /etc/nginx/sites-enabled/berkerpeksag.com')
        sudo('rm /etc/supervisord.conf')


def install():
    """Configures the development environment."""
    local('virtualenv venv')
    with venv():
        local('pip install -r requirements-dev.txt')
        local('cp berkerpeksag/settings_local.py.dist berkerpeksag/settings_local.py')
        local('python manage.py syncdb')


# Development


def server(port='8000'):
    """Starts development server."""
    local('python manage.py runserver %s' % port)


def clean_pyc():
    """Remove all .pyc files."""
    local('find . -name "*.pyc" -exec rm {} \;')

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

    static()
    restart_nginx()


def restart_nginx():
    """Restart the nginx process."""
    sudo('/etc/init.d/nginx restart')


def static():
    """Update static files."""
    with venv():
        put('build', 'build')

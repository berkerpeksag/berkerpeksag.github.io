from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts
from fabric.contrib import project, files

env.hosts = ['berkerpeksag.com']
env.host = env.hosts[0]
env.user = 'wakefield'
env.password = ''
env.project_name = 'berkerpeksag'
env.root = '/home/wakefield/'


def deploy():
    with cd('%(root)s%(project_name)s' % env):
        run('git pull')

    static()


def start():
    """Start the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl start gunicorn' % env)


def stop():
    """Stop the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl stop gunicorn' % env)


def restart():
    """Restart the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl restart gunicorn' % env)


def status():
    """Status of Gunicorn"""
    run('status %(project_name)s' % env)


def restart_nginx():
    sudo('/etc/init.d/nginx restart')


def static():
    with cd('%(root)s%(project_name)s' % env):
        sudo('rm -r static/')
        run('source bin/activate')
        sudo('bin/python manage.py collectstatic')
        restart_nginx()


def update_dependencies():
    """Update requirements remotely."""
    put('requirements.txt', '%(root)s/requirements.txt' % env, use_sudo=True)
    run('%(root)s%(project_name)s/bin/pip install -r %(root)s/requirements.txt' % env)


def configure():
    with cd(env.root):
        run('git clone git://github.com/berkerpeksag/berkerpeksag.git')

    with cd('%(root)s%(project_name)s' % env):
        run('virtualenv --no-site-packages .')
        run('source bin/activate')
        run('%(root)s%(project_name)s/bin/pip install -r %(root)s%(project_name)s/requirements.txt' % env)
        static()
        sudo('ln -s /home/wakefield/berkerpeksag/conf/nginx.conf /etc/nginx/sites-enabled/berkerpeksag.com')
        run('bin/echo_supervisord_conf > supervisord.conf')
        sudo('mv supervisord.conf /etc/supervisord.conf')
        sudo('cat conf/supervisor.conf >> /etc/supervisord.conf')
        run('bin/supervisord')

    put_db()
    restart_nginx()


def setup():
    sudo('apt-get update && apt-get upgrade && apt-get install git-core sqlite3 python-sqlite python-setuptools python-pip python-dev build-essential nginx emacs23 curl libcurl3')
    run('pip install virtualenv')


def put_db():
    put('blog.db', '%(root)s%(project_name)s/blog.db' % env, use_sudo=True)


def delete_db():
    with cd('%(root)s%(project_name)s' % env):
        run('rm *.db')


def clean():
    stop()
    sudo('unlink /tmp/supervisor.sock')

    with cd(env.root):
        sudo('rm -r berkerpeksag/')
        sudo('rm /etc/nginx/sites-enabled/berkerpeksag.com')
        sudo('rm /etc/supervisord.conf')


def clean_pyc():
    """Remove all .pyc files"""
    local('find . -name "*.pyc" -exec rm {} \;')

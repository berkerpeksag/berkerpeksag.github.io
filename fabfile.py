from fabric.api import env, run, cd, sudo, put, local, get

env.hosts = ['berkerpeksag.com']
env.host = env.hosts[0]
env.user = 'wakefield'
env.password = ''
env.project_name = 'berkerpeksag'
env.root = '/home/wakefield/'


def deploy():
    """Deploy the latest version."""
    with cd('%(root)s%(project_name)s' % env):
        run('git pull')

    update_dependencies()
    static()
    restart_nginx()
    restart()


def start():
    """Start the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl start gunicorn' % env)


def stop():
    """Stop the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl stop gunicorn' % env)


def restart():
    """Restart the Gunicorn process"""
    run('%(root)s%(project_name)s/bin/supervisorctl restart gunicorn' % env)


def restart_nginx():
    """Restart the nginx process."""
    sudo('/etc/init.d/nginx restart')


def static():
    """Update static files."""
    with cd('%(root)s%(project_name)s' % env):
        sudo('rm -r static/')
        run('source bin/activate')
        sudo('bin/python manage.py collectstatic --noinput')
        restart_nginx()


def update_dependencies():
    """Update requirements remotely."""
    run('%(root)s%(project_name)s/bin/pip install -ir %(root)s%(project_name)s/requirements.txt' % env)


def configure():
    """Configure basic tools."""
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
    """Setup the VM."""
    sudo('apt-get update && apt-get upgrade && apt-get install git-core sqlite3 python-sqlite python-setuptools python-pip python-dev build-essential nginx emacs23 curl libcurl3')
    run('pip install virtualenv')


def get_db():
    """Get latest database."""
    get('%(root)s%(project_name)s/blog.db' % env, '%(path)s')


def put_db():
    """Upload the database to production."""
    put('blog.db', '%(root)s%(project_name)s/blog.db' % env, use_sudo=True)


def delete_db():
    """Delete the database from production."""
    with cd('%(root)s%(project_name)s' % env):
        run('rm *.db')


def clean():
    """Clean the current setup."""
    stop()
    sudo('unlink /tmp/supervisor.sock')

    with cd(env.root):
        sudo('rm -r berkerpeksag/')
        sudo('rm /etc/nginx/sites-enabled/berkerpeksag.com')
        sudo('rm /etc/supervisord.conf')


def clean_pyc():
    """Remove all .pyc files"""
    local('find . -name "*.pyc" -exec rm {} \;')

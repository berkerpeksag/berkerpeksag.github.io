import os

PROJECT_PATH = os.path.abspath(os.getcwd())

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['berkerpeksag.com', '127.0.0.1', 'localhost']

ADMINS = (
    ('Berker Peksag', 'berker.peksag+blog@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{:s}/dbblog.db'.format(PROJECT_PATH),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = '{:s}/static/'.format(PROJECT_PATH)

STATIC_URL = '/static/'

USE_ETAGS = not DEBUG

STATICFILES_DIRS = (
    '{:s}/blog/static'.format(PROJECT_PATH),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '!a485o-73611(dw4p@f^-ei+=bq2pelf!5mtz6xdi4ku!bm8wt'

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'berkerpeksag.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

CORE_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
)

EXTERNAL_APPS = (
    'gunicorn',
    'south',
    'pipeline',
)

INTERNAL_APPS = (
    'blog',
)

INSTALLED_APPS = CORE_APPS + EXTERNAL_APPS + INTERNAL_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {

    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

PIPELINE_ENABLED = not DEBUG
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'blog.compressors.CssminCompressor'
PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'style/reset.css',
            'style/screen.css',
            'style/pygments.css',
            'style/markdown.css',
        ),
        'output_filename': 'style/screen.min.css',
        'extra_context': {
            'media': 'screen',
        },
        'template_name': 'pipeline/css.jinja',
    },
}

JINJA_CONFIG = {
    'autoescape': False,
    'extensions': ['pipeline.jinja2.ext.PipelineExtension'],
}

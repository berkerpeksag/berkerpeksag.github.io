from settings import *

DEBUG = TEMPLATE_DEBUG = False

USE_ETAGS = not DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{:s}/blog.db'.format(PROJECT_PATH),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

PIPELINE_ENABLED = not DEBUG

# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=i2a.settings.production
from .base import *             # NOQA
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["i2a.com"]
DATABASES = {
    'default': {
        'NAME': 'dbMobileApp',
        'ENGINE': 'sqlserver_pymssql',
        'HOST': '108.60.209.5',  #'sql2501.shared-servers.com',
        'USER': 'userratnesh',
        'PASSWORD': 'Mobile@2018',
        'PORT': 1086,
    }
}
# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = join(dirname(BASE_DIR), 'site', 'static')

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)

ALLOWED_HOSTS += ['i2a.herokuapp.com', 'ec2-34-217-31-164.us-west-2.compute.amazonaws.com']
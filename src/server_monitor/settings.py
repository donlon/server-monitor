"""
Django settings for server_monitor project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import logging
import os
from pathlib import Path

# Get an instance of a logger
logger = logging.getLogger(__name__)
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
      'file': {
         'level': 'DEBUG',
         'class': 'logging.FileHandler',
         'filename': '/tmp/debug.log',
      },
   },
   'loggers': {
      'django': {
         'handlers': ['file'],
         'level': 'DEBUG',
         'propagate': True,
      },
   },
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('APP_SECRET_KEY', 'django-insecure-cfz$bret&(^n=mf)k8vj)b7a+wy-0uiqd!trk8k7%-f+)f-60z')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('APP_PRODUCTION', 'False').lower() == 'false'

ALLOWED_HOSTS = [host for host in os.getenv('APP_ALLOWED_HOSTS', '').split(',') if host]

BEHIND_PROXY = os.getenv('APP_BEHIND_PROXY', 'False').lower() == 'false'

# Application definition

INSTALLED_APPS = [
    'server_monitor.app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_simple_bulma',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server_monitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'server_monitor', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server_monitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
db_path = os.path.join(os.getenv('APP_DB_PATH', BASE_DIR), 'db.sqlite3')

logger.info('Database path: %s' % db_path)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_path,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'server_monitor', 'static')]
STATIC_ROOT = os.path.join(os.getenv('APP_STATIC_FILE_PATH', BASE_DIR), 'tmp', 'staticfiles')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'django_simple_bulma.finders.SimpleBulmaFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom settings for django-simple-bulma
BULMA_SETTINGS = {
    "variables": {  # If you update these colours, please update the notification.css file
        # "primary": "#7289DA",    # Discord blurple
        # "green": "#32ac66",      # Colour picked after Discord discussion
        # "turquoise": "#7289DA",  # Blurple, because Bulma uses this regardless of `primary` above
        # "blue": "#2482c1",       # Colour picked after Discord discussion
        # "cyan": "#2482c1",       # Colour picked after Discord discussion (matches the blue)
        # "purple": "#aa55e4",     # Apparently unused, but changed for consistency
        # "red": "#d63852",        # Colour picked after Discord discussion

        # "link": "$primary",

        "dimensions": "16 24 32 48 64 96 128 256 512",  # Possible image dimensions
        # "navbar-height": "4.75rem",
        # "footer-padding": "1rem 1.5rem 1rem",
        # "tooltip-max-width": "30rem",
    },
    "extensions": [
        "bulma-dropdown",
        "bulma-navbar-burger",
    ],
}

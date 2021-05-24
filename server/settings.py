"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json
import time


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IS_LINUX = BASE_DIR[0] == '/'
IS_WINDOWS = BASE_DIR[1] == ':'

PROJECT_DIR = os.path.join(BASE_DIR, "..", "..")
DEBUG = True

BUILD_MODE = "debug"
if os.path.isfile(os.path.join(PROJECT_DIR, "release")):
    DEBUG = False
    BUILD_MODE = "release"

SETTINGS = None
SETTING_PATH = os.path.join(BASE_DIR, "server", "settings.json")
with open(SETTING_PATH) as f:
    SETTINGS = json.load(f)

VERSION = SETTINGS["version"]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SETTINGS["secrect_key"]

# SECURITY WARNING: don't run with debug turned on in production!

DB_SETTING = SETTINGS["mongodb"][BUILD_MODE]

ALLOWED_HOSTS = ['*']
ADMIN_ENABLED = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'rest_framework',
    'corsheaders',
    'api',
    'web',
    'django_crontab'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

CRONJOBS = [
    ('5 17 * * *', 'server.cron.ScheduleJob')
]
WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' :os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "..", "..", "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "web", "static"),
]

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR,"..", "..", 'media')

if IS_WINDOWS:
    if(MEDIA_ROOT[-1] != "\\"):
        MEDIA_ROOT += "\\"
elif IS_LINUX:
    if(MEDIA_ROOT[-1] != '/'):
        MEDIA_ROOT += '/'

EXCEL_TEMPLATE = os.path.join(BASE_DIR, 'excel')
MEDIA_URL = '/media/'
DATA_UPLOAD_MAX_MEMORY_SIZE = None

CORS_ORIGIN_ALLOW_ALL = True

NUM_FACE = 0
FACE_MIN_SIZE = SETTINGS["face_min_size"]

STREAM_WEBCAM = False

PLAY_WEBCAM = True
WEBCAM_CONNECTED = False

WAITING_TIME = 0
APPEAR_TIME = ""


DISTANCE1 = 0
DISTANCE2 = 0

CURRENT_LOG = ""

GPIO_VALUE =[
    None,  #Pin1 3.3V
    None,  #Pin2 5V
    False, #Pin3 GPIO2
    None,  #Pin4 5V
    False, #Pin5 GPIO3
    None,  #Pin6 GND
    False, #Pin7 GPIO4
    False, #Pin8 GPIO14
    None,  #Pin9 GND
    False, #Pin10 GPIO15
    False, #Pin11 GPIO17
    False, #Pin12 GPIO18
    False, #Pin13 GPIO27
    None,  #Pin14 GND
    False, #Pin15 GPIO22
    False, #Pin16 GPIO23
    None,  #Pin17 3.3V
    False, #Pin18 GPIO24
    False, #Pin19 GPIO10
    None,  #Pin20 GND
    False, #Pin21 GPIO9
    False, #Pin22 GPIO25
    False, #Pin23 GPIO11
    False, #Pin24 GPIO8
    None,  #Pin25 GND
    False, #Pin26 GPIO7
    None,  #Pin27
    None,  #Pin28 
    False, #Pin29 GPIO5
    None,  #Pin30 GND
    False, #Pin31 GPIO6
    False, #Pin32 GPIO12
    False, #Pin33 GPIO13
    None,  #Pin34 GND
    False, #Pin35 GPIO19
    False, #Pin36 GPIO16
    False, #Pin37 GPIO26
    None,  #Pin38 GPIO20
    None,  #Pin39 GND
    False, #Pin40 GPIO21
]
    
"""
Django settings for ecopschat project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import json
import os.path
from pathlib import Path
import dj_database_url
import django_heroku
import environ
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()


env_path=BASE_DIR / ".env"

if env_path.exists():
    with env_path.open(encoding="utf8") as f:
     env.read_env(f, overwrite=True)

# django_channels_layer
if "CHANNEL_LAYER_REDIS_URL" in env:
    channel_layer_redis = env.db_url("CHANNEL_LAYER_REDIS_URL")
    CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                {
                    "host": channel_layer_redis["HOST"],
                    "port": channel_layer_redis.get("PORT") or 6379, # PORT 값이 거짓일 경우 (빈문자열, 0), 디폴트 포트번호로서 6379를 사용
                    "password": channel_layer_redis["PASSWORD"],
                },
            ],
        },
    },
 }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = "django-insecure-ccpa_dgd-*m0a)#nd#u&bhrt&$#i5&u*eu&l4$au9+z-748(&0"



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost','.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'channels',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    "django_bootstrap5",
    "chat",
    "accounts",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ecopschat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "ecopschat" / "templates",
        ],
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

WSGI_APPLICATION = 'ecopschat.wsgi.application'
ASGI_APPLICATION = 'ecopschat.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ounce_db',
        'USER': 'postgres',
        'PASSWORD': 'ewhaecops!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

# Password validation.
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

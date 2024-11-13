"""
Django settings for config project.
"""
import ast
import logging
from os import path, getenv
from pathlib import Path

from django.contrib.messages import constants as messages
from dotenv.main import load_dotenv

load_dotenv('.env')

from utils.common import getenv_or_404

logging.basicConfig(
    level=int(getenv('LOG_LEVEL')),
    format=getenv('LOG_FORMAT')
)

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv_or_404('SECRET_KEY')
DEBUG = ast.literal_eval(getenv_or_404('DEBUG'))
ALLOWED_HOSTS = ['localhost', 'http://127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'task'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'config/templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'PAGE_SIZE': 10
}

# Database
DB_NAME: str = getenv_or_404("DB_NAME")
DB_USER: str = getenv_or_404("DB_USER")
DB_PASSWORD: str = getenv_or_404("DB_PASSWORD")
DB_HOST: str = getenv_or_404("DB_HOST")
DB_PORT: str = getenv_or_404("DB_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
    },
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (path.join(BASE_DIR, 'config/static'),)

# Media config
MEDIA_ROOT = path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = int(getenv('EMAIL_PORT'))
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_PASSWORD')
EMAIL_USE_TLS = ast.literal_eval(getenv_or_404('EMAIL_USE_TLS'))

# Accounts config
LOGIN_REDIRECT_URL = 'api-root'
LOGOUT_REDIRECT_URL = 'api-root'

# Messages Config
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

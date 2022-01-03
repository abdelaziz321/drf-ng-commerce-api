import os
from pathlib import Path
from dotenv import dotenv_values
from datetime import timedelta

ENVIRONMENT_VARIABLES = dotenv_values('.env')


# ---------------------------------- PATHS ---------------------------------- #
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

ROOT_URLCONF = 'project.urls'


# --------------------------- INTERNATIONALIZATION -------------------------- #
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ----------------------------------- APPS ---------------------------------- #
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'rest_framework',

    # Local Apps
    'accounts',
]


# ----------------------------------- DRF ----------------------------------- #
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# -------------------------------- DATABASE --------------------------------- #
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': ENVIRONMENT_VARIABLES['DATABASE_ENGINE'],
        'NAME': ENVIRONMENT_VARIABLES['DATABASE_NAME'],
        'USER': ENVIRONMENT_VARIABLES['DATABASE_USERNAME'],
        'PASSWORD': ENVIRONMENT_VARIABLES['DATABASE_PASSWORD'],
        'HOST': ENVIRONMENT_VARIABLES['DATABASE_HOST'],
        'PORT': ENVIRONMENT_VARIABLES['DATABASE_PORT']
    }
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -------------------------------- SECURITY --------------------------------- #
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENVIRONMENT_VARIABLES['APP_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.Account'

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),    # for debugging
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),   # for debugging

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}


# ------------------------------- MIDDLEWARES ------------------------------- #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------- OTHERS ---------------------------------- #
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

WSGI_APPLICATION = 'project.wsgi.application'

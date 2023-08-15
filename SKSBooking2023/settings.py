"""
Django settings for SKSBooking2023 project.

For more information on this file, see
https://docs.djangoproject.com/

"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent old

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

env_allowed_hosts = []
try:
  env_allowed_hosts = os.environ["ALLOWED_HOSTS"].split(",")
except KeyError:
  pass

ALLOWED_HOSTS = ["localhost"] + env_allowed_hosts




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Application definition
INSTALLED_APPS = [
    'organization',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'bootstrap5',
    'django_bootstrap_icons',
    'rest_framework',
    'Teknik',
    'Sjak',
    'AktivitetsTeam',
    'Butikken',
    'Foto',
    'Location',
    'Depot',
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


ROOT_URLCONF = 'SKSBooking2023.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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



WSGI_APPLICATION = 'SKSBooking2023.wsgi.application'

SCALINGO_POSTGRESQL_URL = 'postgres://sksbooking_9981:qveI-fnqiJHRAbWr26xq@sksbooking-9981.postgresql.a.osc-fr1.scalingo-dbs.com:31234/sksbooking_9981?sslmode=prefer'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
try:
  database_url = os.environ["$SCALINGO_POSTGRESQL_URL"]
except KeyError:
  database_url = "file:///{}".format(os.path.join(BASE_DIR, 'db.sqlite3'))

DATABASES = { 'default': dj_database_url.config() }



#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


# Password validation
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

# Set the authentication backend to use Django's default ModelBackend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'login_user'

# Set the LOGIN_REDIRECT_URL to the URL where you want to redirect the user after successful login
LOGIN_REDIRECT_URL = '/'  # Change the URL to '/' for root URL redirection


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'da-dk'

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AUTH_USER_MODEL = 'organization.Volunteer'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.getenv('EMAIL_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_PASSWORD'))
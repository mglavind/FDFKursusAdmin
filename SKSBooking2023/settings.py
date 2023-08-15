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

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.platformsh.site',
]


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

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#################################################################################
# Platform.shh-specific configuration

# Helper function for decoding base64-encoded JSON variables.
def decode(variable):
    """Decodes a Platform.sh environment variable.
    Args:
        variable (string):
            Base64-encoded JSON (the content of an environment variable).
    Returns:
        An dict (if representing a JSON object), or a scalar type.
    Raises:
        JSON decoding error.
    """
    try:
        if sys.version_info[1] > 5:
            return json.loads(base64.b64decode(variable))
        else:
            return json.loads(base64.b64decode(variable).decode('utf-8'))
    except json.decoder.JSONDecodeError:
        print('Error decoding JSON, code %d', json.decoder.JSONDecodeError)


# This variable must always match the primary database relationship name,
#   configured in .platform.app.yaml.
PLATFORMSH_DB_RELATIONSHIP="database"

# Import some Platform.sh settings from the environment.
# The following block is only applied within Platform.sh environments
# That is, only when this Platform.sh variable is defined
if (os.getenv('PLATFORM_APPLICATION_NAME') is not None):
    DEBUG = False

    # Redefine the static root based on the Platform.sh directory
    # See https://docs.djangoproject.com/en/4.1/ref/settings/#static-root
    if (os.getenv('PLATFORM_APP_DIR') is not None):
        STATIC_ROOT = os.path.join(os.getenv('PLATFORM_APP_DIR'), 'static')

    # PLATFORM_PROJECT_ENTROPY is unique to your project
    # Use it to define define Django's SECRET_KEY
    # See https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key
    if (os.getenv('PLATFORM_PROJECT_ENTROPY') is not None):
        SECRET_KEY = os.getenv('PLATFORM_PROJECT_ENTROPY')

    # Database service configuration, post-build only
    # As services aren't available during the build
    if (os.getenv('PLATFORM_ENVIRONMENT') is not None):
        platformRelationships = decode(os.getenv('PLATFORM_RELATIONSHIPS'))
        db_settings = platformRelationships[PLATFORMSH_DB_RELATIONSHIP][0]
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_settings['path'],
                'USER': db_settings['username'],
                'PASSWORD': db_settings['password'],
                'HOST': db_settings['host'],
                'PORT': db_settings['port'],
            },
            'sqlite': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

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
"""
Django settings for atcoinorg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&eot=(l&g&39+7pkr3v2lt4bsvijqi-qfa-79iwr&7y(*9+&e*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_user',
    'app_entry',
    'app_bank',
    'crispy_forms',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atcoinorg.urls'

WSGI_APPLICATION = 'atcoinorg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASE_ROUTERS = ['atcoinorg.routers.AuthRouter',
                    'atcoinorg.routers.AppEntryRouter',
                    'atcoinorg.routers.AppProfileRouter']

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    DATABASES = {
        'default': {
            'ENGINE': 'djangae.db.backends.appengine'
        },
        'users': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/atcoinorg:users-data',
            'NAME': 'users',
            'USER': 'root'
        }
    }
elif os.getenv('SETTINGS_MODE') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'atcoinorg:users-data',
            'NAME': 'dummy',
        },
        'users': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'atcoinorg:users-data',
            'NAME': 'users',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'djangae.db.backends.appengine'
        },
        'users': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'users',
            'USER': 'root'
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_PROFILE_MODULE = 'app_user.Profile'

FACEBOOK_APP_ID = '1550369835217494'
FACEBOOK_APP_SECRET = '06e9d93d4727719e533dc0ab9a663344'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '&eot=(l&g&39+7pkr3v2lt4bsvijqi-qfa-79iwr&7y(*9+&e*'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.entry',
    'apps.bank',
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
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'atcoinorg.urls'

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

WSGI_APPLICATION = 'atcoinorg.wsgi.application'

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/atcoinorg:data',
            'NAME': 'atcoinorg',
            'USER': 'root'
        }
    }
elif os.getenv('SETTINGS_MODE') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'atcoinorg:atcoinorg',
            'NAME': 'atcoinorg'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'atcoinorg',
            'USER': 'root',
            'PASSWORD': 'britto',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

BUCKET_NAME = 'atcoinorg'

DEFAULT_FILE_STORAGE = 'atcoinorg.storage.GoogleCloudStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_PROFILE_MODULE = 'apps.user.Profile'

FACEBOOK_APP_ID = '1550369835217494'
FACEBOOK_APP_SECRET = '06e9d93d4727719e533dc0ab9a663344'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
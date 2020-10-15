"""
Django settings for grabitapp project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
POSTGRESQL_ADDON_URI="postgresql://ugyucpxiheophshfdyke:DZ4Xom3zZ0SoeK6cLAzv@bvsfwrtlpqtm6oox1xq5-postgresql.services.clever-cloud.com:5432/bvsfwrtlpqtm6oox1xq5"
POSTGRESQL_ADDON_PORT=5432
POSTGRESQL_ADDON_HOST="bvsfwrtlpqtm6oox1xq5-postgresql.services.clever-cloud.com"
POSTGRESQL_ADDON_DB="bvsfwrtlpqtm6oox1xq5"
POSTGRESQL_ADDON_PASSWORD="DZ4Xom3zZ0SoeK6cLAzv"
APP_HOME="/home/greats/grabit/Backend/bikebackend/"
STATIC_URL_PREFIX="/static"
POSTGRESQL_ADDON_USER="ugyucpxiheophshfdyke"
STATIC_URL_PREFIX  = STATIC_URL_PREFIX
MEDIA_ROOT=APP_HOME + STATIC_URL_PREFIX + '/storage/'
MEDIA_URL = "/media/"
STATIC_ROOT = APP_HOME + STATIC_URL_PREFIX + '/static/static/' 

# AWS CREDENTIALS
AWS_RDS_USERNAME='postgres'
AWS_RDS_PASSWORD='nhumeapp123'
SOURVE='209.88.93.187/32'
AWS_RDS_ENDPOINT= 'nhumeapp.c9bwramxwsbn.eu-west-2.rds.amazonaws.com'
AWS_RDS_DBNAME='nhumeapp'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')c^@^^mf^uc5&8!$zdvf2dlw!@-e52&wnuk^2o@&+2e*xx#8rj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '104.243.37.215']


# Application definition

INSTALLED_APPS = [
    'account',
    'mush_store',
    'pages',
    'hotspot',
    'cart',
    'jet',
    'processor',
    'mapwidgets',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'oauth2_provider',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'searchableselect',
    'crispy_forms',
    'mathfilters',
    'django.contrib.gis',
    'django.contrib.postgres.search',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL=True
EASY_MAPS_GOOGLE_KEY = 'AIzaSyC9ZFOeEouLH8gYosPqixfP86djN8iZCVk'
EASY_MAPS_CENTER = (-41.3, 32)
ROOT_URLCONF = 'grabitapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'grabitapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 
# DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis', #''django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
#             'NAME': POSTGRESQL_ADDON_DB,
#             'USER': POSTGRESQL_ADDON_USER,
#             'PASSWORD': POSTGRESQL_ADDON_PASSWORD,
#             'HOST': POSTGRESQL_ADDON_HOST,
#             'PORT': POSTGRESQL_ADDON_PORT,
#             'CONN_MAX_AGE': 5, 
#         }
#     }

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis', #''django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
#             'NAME': AWS_RDS_DBNAME,
#             'USER': AWS_RDS_USERNAME,
#             'PASSWORD': AWS_RDS_PASSWORD,
#             'HOST': AWS_RDS_ENDPOINT,
#             'PORT': POSTGRESQL_ADDON_PORT,
#             'CONN_MAX_AGE': 15, 
#         }
#     }
DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', #''django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
            'NAME': 'effi',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': POSTGRESQL_ADDON_PORT,
            'CONN_MAX_AGE': 15, 
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

# STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [
#     '/static/mush_store/',
# ]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

#Rest
REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
       'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20, 
    
    'DEFAULT_PARSER_CLASSES': (
    'rest_framework.parsers.JSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser',
),

}

#oAuth2 expiration
OAUTH_ACCESS_TOKEN_MODEL = 'oauth2_provider.models.AccessToken'
OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS' : 86400,
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}
MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "gweru"),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'zw'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyC9ZFOeEouLH8gYosPqixfP86djN8iZCVk"
    
}


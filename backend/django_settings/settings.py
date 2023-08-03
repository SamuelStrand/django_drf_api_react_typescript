import os
from datetime import timedelta
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    SECRET_KEY=(str, None),
    ALLOWED_HOSTS=(str, ""),
    DEBUG=(bool, False),
    SQLITE=(bool, True),
    CORS_ALLOW_ALL_ORIGINS=(bool, False),
    CORS_URLS_REGEX=(str, ""),
    SQL_ENGINE=(str, "django.db.backends.sqlite3"),
    SQL_DATABASE=(str, "db.sqlite3"),
    SQL_USER=(str, "django_user"),
    SQL_PASSWORD=(str, "12345"),
    SQL_HOST=(str, "127.0.0.1"),
    SQL_PORT=(str, "5432"),
    POSTGRES_ENGINE=(str, "django.db.backends.sqlite3"),
    POSTGRES_DATABASE=(str, "db.sqlite3"),
    POSTGRES_USER=(str, "django_user"),
    POSTGRES_PASSWORD=(str, "12345"),
    POSTGRES_HOST=(str, "127.0.0.1"),
    POSTGRES_PORT=(str, "5432"),
    REDIS_LOCATION=(str, "rediss://12345@127.0.0.1:3697/0"),
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

SQLITE = env('SQLITE')

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

CORS_ALLOW_ALL_ORIGINS = env('CORS_ALLOW_ALL_ORIGINS')

# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',

    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',

    'django_app',
    'django_api',
]

MIDDLEWARE = [
    "django_app.middleware.CustomCorsMiddleware",
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'react/build'],
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

WSGI_APPLICATION = 'django_settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if SQLITE:
    SQL_ENGINE = env("SQL_ENGINE")
    if SQL_ENGINE == "django.db.backends.sqlite3":
        SQL_DATABASE = Path(BASE_DIR, env("SQL_DATABASE"))
    else:
        SQL_DATABASE = env("SQL_DATABASE")
    SQL_USER = env("SQL_USER")
    SQL_PASSWORD = env("SQL_PASSWORD")
    SQL_HOST = env("SQL_HOST")
    SQL_PORT = env("SQL_PORT")

    DATABASES = {
        "default": {
            "ENGINE": SQL_ENGINE,
            "NAME": SQL_DATABASE,
            "USER": SQL_USER,
            "PASSWORD": SQL_PASSWORD,
            "HOST": SQL_HOST,
            "PORT": SQL_PORT,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": env("POSTGRES_ENGINE"),
            "NAME": env("POSTGRES_DATABASE"),
            "USER": env("POSTGRES_USER"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST"),
            "PORT": env("POSTGRES_PORT"),
        },
        'special': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
        'TIMEOUT': '120',
        'OPTIONS': {
            'MAX_ENTIES': 200,
        }
    },
    'ram_cache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django_ram_cache_table',
    },
    "redis_cache": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        'TIMEOUT': '120',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

CELERY_APP_TIMEZONE = 'Asia/Almaty'
CELERY_APP_TASK_TRACK_STARTED = True
CELERY_APP_TASK_TIME_LIMIT = 1800

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

WSGI_APPLICATION = 'django_settings.wsgi.application'
ASGI_APPLICATION = 'django_settings.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

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

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'eevee.cycle'
EMAIL_HOST_PASSWORD = '31284bogdan'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

host: EMAIL_HOST
port: EMAIL_PORT
username: EMAIL_HOST_USER
password: EMAIL_HOST_PASSWORD
use_tls: EMAIL_USE_TLS
use_ssl: EMAIL_USE_SSL

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = Path(BASE_DIR / 'static')  # todo ENABLE FOR COLLECT STATIC
STATICFILES_DIRS = [
    Path(BASE_DIR / 'static'),  # todo DISABLE FOR COLLECT STATIC
    Path(BASE_DIR, 'react/build/static'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = Path(BASE_DIR, 'static/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('JWT_Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(hours=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=3),
}

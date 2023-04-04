"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')

SECRET_KEY = 'django-insecure-12guxy3p^9by6zg=5mg+14s%-j50vqi+xo_ba(6v9k)2-!m7%2'


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = True
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGINS = [
    "https://fedrelay.com",
    "http://localhost:5173",
]
# Application definition

INSTALLED_APPS = [
    # WHITENOISE ADDED
    "whitenoise.runserver_nostatic",
    
    # Django contrib apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'knox',
    'django_rest_passwordreset',
    

    # Project apps
    'livraison',
    'signup',
    'pointrelais',
    'newsletter',
    'partenariat',
    'contact',
    'profil',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    # WHITENOISE ADDED
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3', 
    # },

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'anaz7484_db_fedrelay_api',
    #     'USER': 'anaz7484_user_fedrelay_api',
    #     'PASSWORD': 'ZW]lVG-]SP?d',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'sql_mode': 'STRICT_ALL_TABLES',
    #     },
    # },

     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fedrelay_db',
        'USER': 'root',
        'HOST': 'localhost',
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

AUTH_USER_MODEL="signup.MyUser"


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# LOCALHOST

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '9ed08af8bbe459'
EMAIL_HOST_PASSWORD = '6877fff64d8445'
EMAIL_PORT = '2525'

# ONLINE HOST
# EMAIL_HOST = 'live.smtp.mailtrap.io'
# EMAIL_HOST_USER = 'api'
# EMAIL_HOST_PASSWORD = '755004a46f869b68af1402fc366a7f36'
# EMAIL_PORT = '587'

# EMAIL_HOST=config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_PORT=config('EMAIL_PORT') 
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')

# MAIL_MAILER=smtp
# MAIL_HOST=send.smtp.mailtrap.io
# MAIL_PORT=587 
# MAIL_USERNAME=api
# MAIL_PASSWORD=6f107884f388997f847e3ec7e1eff41d
# MAIL_ENCRYPTION=tls

# MAIL_FROM_ADDRESS="contact@connect.bj"
# MAIL_FROM_NAME="${APP_NAME}"

# Make sure that BASE_DIR is defined somewhere at the top
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = BASE_DIR / "staticfiles"
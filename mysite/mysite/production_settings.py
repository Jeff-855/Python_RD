# Import all default settings.
from .settings import *

import dj_database_url


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  #PostgreSQL
        'NAME': 'd648rd7mjivgot',        #資料庫名稱
        'USER': 'cgnhzkzooignln',      #資料庫帳號
        'PASSWORD': '9abdc56a2a5eb8577433249138fa2c0637e712bb976a5aeb0d01b9501084260b',  #資料庫密碼
        'HOST': 'ec2-34-239-33-57.compute-1.amazonaws.com',     #Server(伺服器)位址
        'PORT': '5432'           #PostgreSQL Port號
    }
}
#DATABASES = {
#   'default': dj_database_url.config(),
#}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'mysite'
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'



# Static asset configuration.
#STATIC_ROOT = 'staticfiles'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = True

#STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR:"+BASE_DIR)
#BASE_DIR='/mysite/mysite'
print("BASE_DIR1:"+BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
#print("STATICFILES_DIRS:"+STATICFILES_DIRS)
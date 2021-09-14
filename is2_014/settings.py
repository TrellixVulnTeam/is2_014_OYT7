# """
# Django settings for is2_014 project.
#
# Generated by 'django-admin startproject' using Django 3.2.6.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.2/ref/settings/
# """
#
# #se importa la libreria path
#
# from pathlib import Path
# import dj_database_url
# import os
# from decouple import config
#
# # se indica la direccion base del path
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
#
# # ADVERTENCIA DE SEGURIDAD: mantenga la clave secreta utilizada en producción en secreto!
#
# #SECRET_KEY = 'django-insecure-#%-!0%=56hnp7+4f1wy1ucxx**)-2-uvz)mb=tbf$#ga8==4+-'
#
#
#
# # ADVERTENCIA DE SEGURIDAD: no ejecute con la depuración activada en producción!
#
# DEBUG = False
#
#
# ALLOWED_HOSTS = ['app014is2.herokuapp.com', '127.0.0.1']
# SECRET_KEY = os.environ.get('SECRET_KEY')
#
#
# # Definicion de las aplicaciones instaladas
#
#INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.sites',
#     'Inicio',
#     'proyecto',
#     'usuarios',
#     'rol',
#     'flujo',
#     'tipoUserStory',
#     'userstory',
#     'sprint',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]
#
# ROOT_URLCONF = 'is2_014.urls'
#
# #Plantillas
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'is2_014.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#
# #DATABASES = {
#  #   'default': {
#   #      'ENGINE': 'django.db.backends.sqlite3',
#    #     'NAME': BASE_DIR / 'db.sqlite3',
#     #}
# #}
#
# #definimos la base de datos y la configuramos
#
# DATABASES = {
#     #'default': {
#     #   'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     #    'NAME': 'sistemagestor',
#     #    'USER': 'postgres',
#     #    'PASSWORD':'postgres',
#     #    'HOST':'localhost',
#     #    'PORT': '5432',
#     #}
# 'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
#
# }
#
# # validacion de contraseñas
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/
#
# LANGUAGE_CODE = 'es'
#
# TIME_ZONE = 'America/Asuncion'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'static'),
# ]
#
# STATICFILES_FINDERS =[
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# ]
#AUTH_USER_MODEL = 'usuarios.Usuario'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
#
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# #configuramos django como backend de autentificacion
#
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend'
# ]
# #para los proveedores de cuentas sociales configuramos a google
#
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }
# #se agrega un sitio ID y se redirije a los usuarios a una ruta base despues del Inicio de sesion
#
# SITE_ID = 2
#
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # procedere a hacer dos settings



###############################################################################################################################3
#se importa la libreria path
import os
from pathlib import Path

# se indica la direccion base del path

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: mantenga la clave secreta utilizada en producción en secreto!

SECRET_KEY = 'django-insecure-#%-!0%=56hnp7+4f1wy1ucxx**)-2-uvz)mb=tbf$#ga8==4+-'

# ADVERTENCIA DE SEGURIDAD: no ejecute con la depuración activada en producción!

DEBUG = True

ALLOWED_HOSTS = []


# Definicion de las aplicaciones instaladas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'Inicio',
    'proyecto',
    'usuarios',
    'rol',
    'flujo',
    'tipoUserStory',
    'userstory',
    'sprint',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'is2_014.urls'

#Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'is2_014.wsgi.application'




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}

#definimos la base de datos y la configuramos

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistemagestor',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST':'localhost',
        'PORT': '5432',
    }
}

# validacion de contraseñas
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

STATICFILES_FINDERS =[
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#configuramos django como backend de autentificacion

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
#para los proveedores de cuentas sociales configuramos a google

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
#se agrega un sitio ID y se redirije a los usuarios a una ruta base despues del Inicio de sesion

SITE_ID = 2

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'usuarios.Usuario'

from .base import *
import os
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'andres',
        'PASSWORD': 'cursopro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'd2td91ebvm79ck',
#         'USER': 'tgvnbylrqgyspl',
#         'PASSWORD': '7a26e847e643608037a3b84833f61dbe4eda8dfcefbeca0d1bbf7ff78ae6d69a',
#         'HOST': 'ec2-3-227-15-75.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }


#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
# django_heroku.settings(locals())
#STATIC_ROOT = (BASE_DIR + "static")
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_DIRS = [BASE_DIR.child('static')]
#STATICFILE_DIRS = [BASE_DIR + "static", "empleado/static"]
#STATICFILE_DIRS = [BASE_DIR + "static", ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

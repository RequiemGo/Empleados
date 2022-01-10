from .base import *
import os
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


STATIC_URL = '/static/'
#STATIC_ROOT = (BASE_DIR + "static")
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_DIRS = [BASE_DIR.child('static')]
#STATICFILE_DIRS = [BASE_DIR + "static", "empleado/static"]
#STATICFILE_DIRS = [BASE_DIR + "static", ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

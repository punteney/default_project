from base import *

DEBUG = True

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_HOST = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_OPTIONS = {}

SECRET_KEY = '50%_6q*splag)qsd@(zklf(w@4=4n!(6$@kv!4!v_maw47u6bi'

BASE_DOMAIN = ''
#MEDIA_URL = ''


SSL_ENABLED = False
SEND_BROKEN_LINK_EMAILS = False
SESSION_COOKIE_DOMAIN = '.%s' % BASE_DOMAIN

#UPLOAD_URL = MEDIA_URL + 'uploads/'

# Local Cache Settings
#CACHE_BACKEND = 'memcached://172.20.1.127:11211/'

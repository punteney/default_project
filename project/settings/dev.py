from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'recipes'
DATABASE_USER = 'recipes'
DATABASE_PASSWORD = 'pass12345'

SSL_ENABLED = False

# Cache Settings
CACHE_BACKEND = 'dummy://'

BASE_DOMAIN = 'oscar1.com'
SESSION_COOKIE_DOMAIN = '.%s' % BASE_DOMAIN
BASE_DOMAIN = BASE_DOMAIN + ':8000'


def custom_show_toolbar(request):
    return True # Toggle to show toolbar or not, much slower with toolbar.
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar','django_extensions',)

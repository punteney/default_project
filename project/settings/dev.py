from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_NAME = ''
DATABASE_USER = ''
# DATABASE_PASSWORD = ''

# Settings if using sqlite
# DATABASE_ENGINE = 'sqlite3'
# DATABASE_NAME = os.path.join(PROJECT_PATH, 'data/dev.db')

SSL_ENABLED = False

# Cache Settings
CACHE_BACKEND = 'dummy://'

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar','django_extensions',)

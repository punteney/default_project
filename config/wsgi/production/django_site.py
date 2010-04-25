import os
import sys

sys.path.appen(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))) #Moving up to the top projct dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['CONFIG_IDENTIFIER'] = 'production'

# Setting whether SSL or Not
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    environ['wsgi.url_scheme'] = environ.get('HTTP_X_URL_SCHEME', 'http') 
    return _application(environ, start_response)


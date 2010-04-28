import os
import site
import sys

# Adding the virtual_env directory
# If the virtual_env is in a different spot update this
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../v_env/lib/python2.6/site-packages")))

# Adding the project level directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))) #Moving up to the top projct dir

# If the project isn't in the 'project' dir, set the below to match 
# your project
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ENVIRONMENT'] = 'production'

# Setting whether SSL or Not
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    environ['wsgi.url_scheme'] = environ.get('HTTP_X_URL_SCHEME', 'http') 
    return _application(environ, start_response)


from django.conf import settings
from django.test.simple import run_tests as run_tests_orig

def _setup_mongo():
    from mongoengine import connect
    # Connecting to a test DB for Mongo
    settings.MONGO_DB_NAME = 'test_'+settings.MONGO_DB_NAME
    connect(settings.MONGO_DB_NAME)  

def _teardown_mongo():
    from pymongo import Connection
    # Destroying the test database
    c = Connection()
    c.drop_database('settings.MONGO_DB_NAME')    

def _setup_celery():
    settings.CELERY_ALWAYS_EAGER = True

def run_tests(test_labels, *args, **kwargs):
    """Django test runner allowing testing of celery delayed tasks
and setting the mongo db to be a test DB.
 
For celery All tasks are run locally, not in a worker.
 
"""
    with_mongo = False
    if hasattr(settings, 'MONGO_DB_NAME'):
        with_mongo = True
    with_celery = False
    if 'celery' in settings.INSTALLED_APPS:
        with_celery = True

    if with_mongo:
        _setup_mongo()
    if with_celery:
        _setup_celery()
    
    return run_tests_orig(test_labels, *args, **kwargs)

    if with_mongo:
        _teardown_mongo()



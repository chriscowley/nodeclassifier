from fabric.api import *

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def test():
    local('python test.py')

def serve():
    local('python manage.py runserver')

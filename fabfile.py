from fabric.api import local
import os

D51_DJANGO_PACKAGES = [
    'd51.django.apps.blogs',
    'd51.django.apps.invites',
    'd51.django.apps.logger',
    'd51.django.apps.schedules',
    'd51.django.apps.sharing',
    'd51.django.apps.tagging',
    'd51.django.apps.twitter',
    'd51.django.auth',
    'd51.django.db.models.generic',
    'd51.django.virtualenv.test_runner',
]

def src():
    for package in D51_DJANGO_PACKAGES:
        if not os.path.exists('src/%s' % package):
            repo = "git://github.com/domain51/%s.git" % package
            local('git clone %s src/%s' % (repo, package))
        else:
            os.chdir('src/%s' % package)
            local('git pull origin')
            os.chdir('../..')

        local('cp -R src/%s/d51 .' % package)

def setup(type):
    src()
    if os.path.exists('MANIFEST'):
        local('rm MANIFEST')
    local('python setup.py %s' % type)

def build():
    setup('build')

def install():
    setup('install')

def sdist():
    setup('sdist')

def clean():
    local('rm -rf build/ d51/ src/ dist/  MANIFEST')

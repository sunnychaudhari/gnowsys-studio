
# Copyright (c) 2011,  2012 Free Software Foundation

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""This file has the settings for Gstudio Demo"""
import os
TIME_ZONE = None
gettext = lambda s: s
direxist=os.path.isdir("/tmp/beta/")
if not direxist:
    os.system("mkdir /tmp/beta/")
DEBUG = True
TEMPLATE_DEBUG78 = True
#INTERNAL_IPS = ('127.0.0.1','158.144.44.212','158.144.42.67')
#DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT-REDIRECTS':False,}
DATABASES = {'default':
             {'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(os.path.dirname(__file__), 'demo.db')}
             }

STATIC_URL = '/static/'
STATIC_ROOT = '/static'
RECAPTCHA_PUBLIC_KEY = '6LcBr9USAAAAAJNHxpA5_2nQK9JnKQCU3kTUstEK'
RECAPTCHA_PRIVATE_KEY = '6LcBr9USAAAAABYW6VgsQeupDHy2R42G4aGsHxXr'
MEDIA_URL = '/static'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/img')
MEDIA_ROOTNEW2 = os.path.join(os.path.dirname(__file__), 'static/img')
MEDIA_ROOTNEW3 = os.path.join(os.path.dirname(__file__), 'static/img')
MEDIA_ROOTNEW4 = os.path.join(os.path.dirname(__file__), 'static/img/Subicons')
MEDIA_ROOTNEW5 = os.path.join(os.path.dirname(__file__), 'static/img/Vericons')
MEDIA_ROOTNEW6 = os.path.join(os.path.dirname(__file__), 'static/img/Objicons')
#MEDIA_ROOTNEW = os.path.join(os.path.dirname(__file__), 'static/img')
MEDIA_ROOTNEW = os.path.join(os.path.dirname(__file__), '../demo/media')
#MEDIA_ROOT = '/static'
#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../gstudio/static')
PYSCRIPT_URL_GSTUDIO = os.path.join(os.path.dirname(__file__), '../gstudio/createhtml.py')
PYSCRIPT_URL_OBJECTAPP = os.path.join(os.path.dirname(__file__), '../objectapp/createhtml.py')
HTML_FILE_URL=os.path.join(os.path.dirname(__file__),'../demo/static/grappelli/file/')
VIDEO_PANDORA_URL = os.getenv("HOME")+"/.ox/client.json"
FILE_URL = os.path.join(os.path.dirname(__file__), '/tmp/beta/')
FILE_UPLOAD_MAX_MEMORY_SIZE= 524288000
JPEG_ROOT = None
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__),'grappelli/static'),
)

GSTUDIO_UPLOAD_TO = 'static/img/'

ADMIN_MEDIA_PREFIX = STATIC_URL 

SECRET_KEY = 'jo-1rzm(%sf)3#n+fb7h955yu$3(pt63abhi12_t7e^^5q8dyw'

USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'en'

GRAPPELLI_ADMIN_TITLE = '<a href="/" title="Gnowledge Studio">Gnowledge Studio</a>'

GRAPPELLI_INDEX_DASHBOARD = "demo.dashboard.CustomIndexDashboard"

GSTUDIO_RDF_FILEPATH = os.path.join(os.path.dirname(__file__), 'rdffiles.rdf')

# Authentication related
ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'webmaster@beta.metastudio.org'
LOGIN_REDIRECT_URL = '/'

# fourstore related
FOURSTORE_KBNAME = "demo"  # Name of 4store knowledge base
FOURSTORE_PORT = 8067      # Port for 4store HTTP server
SPARQL_ENDPOINT = "http://localhost:8067/sparql/"






LANGUAGES = (('en', gettext('English')),
             ('fr', gettext('French')),
             ('de', gettext('German')),
             ('es', gettext('Spanish')),
             ('it', gettext('Italian')),
             ('nl', gettext('Dutch')),
             ('hu', gettext('Hungarian')),
             ('ru', gettext('Russian')),
             ('pl', gettext('Polish')),
             ('pt_BR', gettext('Brazilian Portuguese')),
             ('zh_CN', gettext('Simplified Chinese')),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    )

ROOT_URLCONF = 'demo.urls'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
        )
     ),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'gstudio.context_processors.version',
    'objectapp.context_processors.version',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'mptt',
    'reversion',
    'tagging',
    'markitup',
    'django_xmlrpc',
    'grappelli.dashboard',
    'grappelli',
    'gstudio',
    'objectapp',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'djangoratings',
    'registration',
    'graphviz',
    'demo',
    'fourstore',
    'HTTP4Store',
    'html5lib',
    'pagination',
    'notification',
    'fixture_magic',
    # Uncomment the south entry to activate south for database migrations
    # Please do install south before uncommenting
    # command: sudo pip install south 
    #'south',
    )


#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


from gstudio.xmlrpc import GSTUDIO_XMLRPC_METHODS
XMLRPC_METHODS = GSTUDIO_XMLRPC_METHODS
try:
    from local_settings import *
    #print "Local settings applied"
except:
    #print "Default settings applied"
    pass

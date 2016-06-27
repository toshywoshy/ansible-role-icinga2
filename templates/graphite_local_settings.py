###
### --------------------------------------------------
### VanTosh Graphite Config File
### (c) copyleft 2013 VanTosh
### Author: Toshaan Bharvani <toshaan@vantosh.com>
### --------------------------------------------------
### {{ ansible_managed }}
###


#SECRET_KEY = 'UNSAFE_DEFAULT'
#ALLOWED_HOSTS = [ '*' ]
TIME_ZONE = 'Europe/Brussels'
#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True
#LOG_METRIC_ACCESS = True
#DEBUG = True
#FLUSHRRDCACHED = 'unix:/var/run/rrdcached.sock'
#MEMCACHE_HOSTS = ['10.10.10.10:11211', '10.10.10.11:11211', '10.10.10.12:11211']
#DEFAULT_CACHE_DURATION = 60 # Cache images and data for 1 minute
GRAPHITE_ROOT = '/usr/share/graphite'
CONF_DIR = '/etc/graphite-web'
STORAGE_DIR = '/var/lib/graphite-web'
CONTENT_DIR = '/usr/share/graphite/webapp/content'
#DASHBOARD_CONF = '/etc/graphite-web/dashboard.conf'
#GRAPHTEMPLATES_CONF = '/etc/graphite-web/graphTemplates.conf'
WHISPER_DIR = '/var/lib/carbon/whisper/'
RRD_DIR = '/var/lib/carbon/rrd'
DATA_DIRS = [WHISPER_DIR, RRD_DIR] # Default: set from the above variables
LOG_DIR = '/var/log/graphite-web/'
INDEX_FILE = '/var/lib/graphite-web/index'  # Search index file
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = False
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
#USE_LDAP_AUTH = True
#LDAP_SERVER = "ldap.mycompany.com"
#LDAP_PORT = 389
#LDAP_URI = "ldaps://ldap.mycompany.com:636"
#LDAP_SEARCH_BASE = "OU=users,DC=mycompany,DC=com"
#LDAP_BASE_USER = "CN=some_readonly_account,DC=mycompany,DC=com"
#LDAP_BASE_PASS = "readonly_account_password"
#LDAP_USER_QUERY = "(username=%s)"  #For Active Directory use "(sAMAccountName=%s)"
#import ldap
#ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
#ldap.set_option(ldap.OPT_X_TLS_CACERTDIR, "/etc/ssl/ca")
#ldap.set_option(ldap.OPT_X_TLS_CERTFILE, "/etc/ssl/mycert.pem")
#ldap.set_option(ldap.OPT_X_TLS_KEYFILE, "/etc/ssl/mykey.pem")
#USE_REMOTE_USER_AUTHENTICATION = True
#LOGIN_URL = '/account/login'
DATABASES = {
    'default': {
        'NAME': '/var/lib/graphite-web/storage/graphite.db3',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
#CLUSTER_SERVERS = ["10.0.2.2:80", "10.0.2.3:80"]
#REMOTE_STORE_FETCH_TIMEOUT = 6   # Timeout to fetch series data
#REMOTE_STORE_FIND_TIMEOUT = 2.5  # Timeout for metric find requests
#REMOTE_STORE_RETRY_DELAY = 60    # Time before retrying a failed remote webapp
#REMOTE_FIND_CACHE_DURATION = 300 # Time to cache remote metric find results
#REMOTE_RENDERING = True
#RENDERING_HOSTS = []
#REMOTE_RENDER_CONNECT_TIMEOUT = 1.0
#CARBONLINK_HOSTS = ["127.0.0.1:7002:a", "127.0.0.1:7102:b", "127.0.0.1:7202:c"]
#CARBONLINK_TIMEOUT = 1.0
#from graphite.app_settings import *

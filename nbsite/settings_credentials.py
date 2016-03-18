# 
# uncomment and complete the following to set up your server name
#
#NB_SERVERNAME = ""

# 
# uncomment and complete the following to set up who should get cron reports
#
#CRON_EMAIL = ""

# 
# These are overrides to defaults set in settings.py.  To keep defaults, leave
# these values empty. To replace the defaults, uncomment the line and enter 
# your changes here rather than making the changes in settings.py.
#
# DEBUG = ""
# TEMPLATE_DEBUG = ""
# ADMINS = (('admin name', 'admin@admin.test'),)
# MANAGERS = ""
# NB_HTTP_PORT = ""
# HTTPD_MEDIA = ""
# HTTPD_MEDIA_CACHE = ""
# EMAIL_HOST = ""
# EMAIL_FROM = ""
# EMAIL_BCC = ""

# EMAIL_BACKEND = ""
# EMAIL_FILE_PATH = ""

# PERSONA_EMAIL = ""
# PERSONA_PASSWORD = ""

# Make this unique, and don't share it with anybody.
SECRET_KEY = "CHANGE_ME"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nota-bene DB',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
FACEBOOK_APP_ID         = "CHANGE_ME"
FACEBOOK_APP_SECRET     = "CHANGE_ME"
GOOGLE_DEVELOPER_KEY    = "CHANGE_ME"

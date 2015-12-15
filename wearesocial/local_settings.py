import os
from settings import BASE_DIR, INSTALLED_APPS

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# INSTALLED_APPS += ('debug_toolbar',)

TEMPLATE_DEBUG = True
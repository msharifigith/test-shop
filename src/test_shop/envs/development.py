from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djshop',
        'USER': 'djshop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}
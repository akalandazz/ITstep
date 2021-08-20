from .base import *

DEBUG = False

ADMINS = (
	('Amiran K', 'amurikokalandia@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'educa',
		'USER': 'kalandazpostgre',
		'PASSWORD': 'kalandaz123',
		'HOST': 'localhost',
		'PORT':'5432',
		
		}
	}


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

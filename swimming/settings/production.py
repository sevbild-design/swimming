from swimming.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['89.108.76.34']

STATIC_ROOT = '/root/wantedpa/swimming/static'
STATIC_URL = '/static/'

# # Безопасность в продакшене
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
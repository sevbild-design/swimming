from swimming.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['89.108.76.38']

# STATIC_ROOT = '/var/www/swimming_static'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# # Безопасность в продакшене
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
from swimming.settings.base import *


DEBUG = False
ALLOWED_HOSTS = [
    'wantedpa.pythonanywhere.com/',
    'www.wantedpa.pythonanywhere.com/'
]

STATIC_ROOT = '/home/wantedpa/swimming/static'

# Безопасность в продакшене
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
from swimming.settings.base import *


DEBUG = True
ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'sevbild.ru',
    'www.sevbild.ru',
    'sevbild.online',
    'www.sevbild.online',    
]

# Дополнительные настройки для разработки
INTERNAL_IPS = ['127.0.0.1']  # для django-debug-toolbar
STATIC_ROOT = BASE_DIR / 'staticfiles'

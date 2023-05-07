from .base import *
import os

#서버용

ALLOWED_HOSTS = ['43.200.120.132','junheemerong.kr']
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [BASE_DIR / 'static']
DEBUG = False
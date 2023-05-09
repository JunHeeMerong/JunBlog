from .base import *
import os

#서버용

ALLOWED_HOSTS = ['43.200.120.132','junheemerong.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True
"""
WSGI config for tubodega project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tubodega.settings")

application = get_wsgi_application()
#los de abajo es para heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

# from django.db import models

# Create your models here.
import os

settings = os.environ.get("DJANGO_SETTINGS_MODULE")

if settings == "monian.settings":
    from monian.settings import STATICFILES_DIRS
else:
    from monian.dev_settings import STATICFILES_DIRS


class Category(object):

    def list(self):
        print STATICFILES_DIRS
        self.categories = os.listdir(STATICFILES_DIRS[0])
        return self.categories

# from django.db import models

# Create your models here.
import os

settings = os.environ.get("DJANGO_SETTINGS_MODULE")

if settings == "monian.settings":
    from monian.settings import STATICFILES_DIRS
else:
    from monian.dev_settings import STATICFILES_DIRS


class Category(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def list():
        str_categories = os.listdir(STATICFILES_DIRS[0])
        str_categories.sort()
        categories = [Category(name) for name in str_categories]
        return categories

    @property
    def pictures(self):
        pics = os.listdir(os.path.join(STATICFILES_DIRS[0] + '/' + self.name))
        pics.sort()
        return [Picture(name) for name in pics]


class Picture(object):

    def __init__(self, name):
        self.name = name

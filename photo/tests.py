"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from unittest import TestCase
from photo.models import Category


class CategoryTest(TestCase):

    def test_get_category(self):
        category = Category()
        categories = category.list()
        self.assertEqual(len(categories), 2)
        self.assertEqual(categories, ['cool', 'super_hero'])

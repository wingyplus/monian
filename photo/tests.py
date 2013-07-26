"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
import unittest
from photo.models import Category, Picture


class CategoryTest(unittest.TestCase):

    def test_get_categories(self):
        categories = Category.list()
        self.assertEqual(len(categories), 2)

    def test_get_categories_should_be_instance_of_Category(self):
        categories = Category.list()
        self.assertIsInstance(categories[0], Category)
        self.assertEqual(categories[0].name, "cool")
        self.assertIsInstance(categories[1], Category)
        self.assertEqual(categories[1].name, "super_hero")

    def test_len_pictures_from_category(self):
        category = Category("super_hero")
        pics = category.pictures

        self.assertEqual(len(pics), 3)

    def test_instance_pictures_when_get_from_category(self):
        category = Category("super_hero")
        pics = category.pictures

        self.assertIsInstance(pics[0], Picture)
        self.assertEqual(pics[0].name, 'a.jpg')
        self.assertIsInstance(pics[1], Picture)
        self.assertEqual(pics[1].name, 'b.jpg')
        self.assertIsInstance(pics[2], Picture)
        self.assertEqual(pics[2].name, 'c.jpg')

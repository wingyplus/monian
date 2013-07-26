# Create your views here.
from django.shortcuts import render
from photo.models import Category


def index(req):
    categories = Category.list()
    return render(req, "category/index.html", {"categories": categories})

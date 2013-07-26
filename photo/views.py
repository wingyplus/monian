# Create your views here.
from django.shortcuts import render


def index(req):
    return render(req, "category/index.html")

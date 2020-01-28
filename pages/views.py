from django.shortcuts import render
from django.http import HttpResponse

def index(reuqest):
    return HttpResponse('<h1>Hello World</h1>')


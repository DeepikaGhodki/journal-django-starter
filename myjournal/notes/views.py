from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're reading my notes")


def notebook(request, notebook_id):
    return HttpResponse("This is a notebook")


def note(request, note_id):
    return HttpResponse("This is a note")

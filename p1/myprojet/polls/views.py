from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse


def index(request):
    html = '<html lang="en"><body>Hello... world. You\'re at the polls index..</body></html>'
    return HttpResponse(html)
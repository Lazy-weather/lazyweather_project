from django.shortcuts import render
from django.http import HttpResponse


def page(request):
    return render(request, 'index.html')

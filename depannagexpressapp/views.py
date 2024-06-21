from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'depannagexpressapp/index.html')

def remorquage_simple(request):
    return render(request, 'depannagexpressapp/remorquage-simple.html')

def repsur_place(request):
    return render(request, 'depannagexpressapp/repsur-place.html')

def remorquage_reparation(request):
    return render(request, 'depannagexpressapp/remorquage-reparation.html')

def contact(request):
    return render(request, 'depannagexpressapp/contact.html')

def apropos(request):
    return render(request, 'depannagexpressapp/apropos.html')

def show_base_dir(request):
    return HttpResponse(f"BASE_DIR: {settings.BASE_DIR}")

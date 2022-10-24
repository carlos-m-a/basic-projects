from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    return render (request=request, template_name="base/home.html")

def index(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect(settings.LOGIN_URL)
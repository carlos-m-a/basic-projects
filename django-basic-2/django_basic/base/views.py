from django.shortcuts import render, redirect


def home(request):
    return render (request=request, template_name="base/home.html")
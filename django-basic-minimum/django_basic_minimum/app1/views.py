from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request=request, template_name="app1/home.html")
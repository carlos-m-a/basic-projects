from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def get_books(request):
    return render(request=request, template_name="accounts/register.html")
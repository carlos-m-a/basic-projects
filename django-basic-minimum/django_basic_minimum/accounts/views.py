from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf import settings
from django.core.exceptions import ValidationError
from django.views import generic, View
from django.views.generic.edit import UpdateView
from .forms import NewUserForm, UpdateUserForm, DeleteUserForm
from django.contrib.auth.hashers import check_password


class RegisterView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


@login_required
def update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            context = {'form': form,}
            return render(request, 'profile/update.html', context)
    else:
        form = UpdateUserForm(instance=request.user)
        context = {'form': form,}
        return render(request, 'profile/update.html', context)


@login_required
def delete(request):
    user:User = request.user
    if request.method == 'POST':
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if not check_password(password, user.password):
                form.add_error('password', 'Incorrect password')
                context = {'form': form,}
                return render(request, 'profile/delete.html', context)
            else:
                user.is_active = False
                user.save()
                logout(request)
                return redirect(settings.LOGIN_URL)
    else:
        form = DeleteUserForm()
        context = {'form': form,}
        return render(request, 'profile/delete.html', context)


@login_required
def profile(request):
    return render(request, 'profile/profile.html')
            
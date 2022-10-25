from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf import settings
from django.views import generic
from .forms import NewUserForm, UpdateUserForm, DeleteUserForm
from django.contrib.auth.hashers import check_password

VIEW_PROFILE_TEMPLATE_FILE = 'profile/profile.html'
UPDATE_PROFILE_TEMPLATE_FILE = 'profile/update.html'
DELETE_PROFILE_TEMPLATE_FILE = 'profile/delete.html'
REGISTER_USER_TEMPLATE_FILE = 'registration/register.html'
REGISTER_USER_DONE_TEMPLATE_FILE = 'registration/register_done.html'

class RegisterView(generic.CreateView):
    form_class = NewUserForm
    template_name = REGISTER_USER_TEMPLATE_FILE
    def form_valid(self, form):
        form.save()
        context = {}
        context['new_user_name'] = form.cleaned_data['username']
        context['new_user_email'] = form.cleaned_data['email']
        return render(self.request, REGISTER_USER_DONE_TEMPLATE_FILE, context)


@login_required
def update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            context = {'form': form,}
            return render(request, UPDATE_PROFILE_TEMPLATE_FILE, context)
    else:
        form = UpdateUserForm(instance=request.user)
        context = {'form': form,}
        return render(request, UPDATE_PROFILE_TEMPLATE_FILE, context)


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
                return render(request, DELETE_PROFILE_TEMPLATE_FILE, context)
            else:
                user.is_active = False
                user.save()
                logout(request)
                return redirect(settings.LOGIN_URL)
    else:
        form = DeleteUserForm()
        context = {'form': form,}
        return render(request, DELETE_PROFILE_TEMPLATE_FILE, context)


@login_required
def profile(request):
    return render(request, VIEW_PROFILE_TEMPLATE_FILE)
            
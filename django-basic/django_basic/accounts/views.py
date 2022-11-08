from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import logout, get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.conf import settings
from django.views import generic
from .forms import NewUserForm, UpdateUserForm, DeleteUserForm, NewAuthenticationForm, NewPasswordChangeForm, NewPasswordResetForm, NewSetPasswordForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

User = get_user_model()


VIEW_PROFILE_TEMPLATE_FILE = 'accounts/profile.html'
UPDATE_PROFILE_TEMPLATE_FILE = 'accounts/update.html'
DELETE_PROFILE_TEMPLATE_FILE = 'accounts/delete.html'
REGISTER_USER_TEMPLATE_FILE = 'accounts/register.html'
REGISTER_USER_DONE_TEMPLATE_FILE = 'accounts/register_done.html'
LOGIN_TEMPLATE_FILE = 'accounts/login.html'
LOGOUT_TEMPLATE_FILE = 'accounts/logged_out.html'
PASSWORD_CHANGE_TEMPLATE_FILE = 'accounts/password_change_form.html'
PASSWORD_CHANGE_DONE_TEMPLATE_FILE = 'accounts/password_change_done.html'
PASSWORD_RESET_TEMPLATE_FILE = 'accounts/password_reset_form.html'
PASSWORD_RESET_DONE_TEMPLATE_FILE = 'accounts/password_reset_done.html'
PASSWORD_RESET_CONFIRM_TEMPLATE_FILE = 'accounts/password_reset_confirm.html'
PASSWORD_RESET_COMPLETE_TEMPLATE_FILE = 'accounts/password_reset_complete.html'
EMAIL_TEMPLATE_FILE = 'accounts/password_reset_email.html'
SUBJECT_EMAIL_TEMPLATE_FILE = 'accounts/password_reset_subject.txt'


def raise_404_if_authenticated(request):
    if request.user.is_authenticated:
        raise Http404


class RegisterView(generic.CreateView):
    form_class = NewUserForm
    template_name = REGISTER_USER_TEMPLATE_FILE
    def form_valid(self, form):
        form.save()
        context = {}
        context['new_user_name'] = form.cleaned_data['username']
        context['new_user_email'] = form.cleaned_data['email']
        return render(self.request, REGISTER_USER_DONE_TEMPLATE_FILE, context)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class NewLoginView(LoginView):
    template_name = LOGIN_TEMPLATE_FILE
    authentication_form = NewAuthenticationForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class NewLogoutView(LogoutView):
    template_name = LOGOUT_TEMPLATE_FILE
    def get(self, request, *args, **kwargs):
        raise Http404

class NewPasswordChangeView(PasswordChangeView):
    template_name = PASSWORD_CHANGE_TEMPLATE_FILE
    success_url = reverse_lazy('accounts:profile')
    form_class = NewPasswordChangeForm
    def form_valid(self, form):
        messages.success(self.request, _('Password has changed'))
        return super().form_valid(form)

class NewPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = PASSWORD_CHANGE_DONE_TEMPLATE_FILE

class NewPasswordResetView(PasswordResetView):
    template_name = PASSWORD_RESET_TEMPLATE_FILE
    email_template_name = EMAIL_TEMPLATE_FILE
    subject_template_name = SUBJECT_EMAIL_TEMPLATE_FILE
    success_url = reverse_lazy('accounts:password_reset_done')
    form_class = NewPasswordResetForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class NewPasswordResetDoneView(PasswordResetDoneView):
    template_name = PASSWORD_RESET_DONE_TEMPLATE_FILE
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class NewPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = PASSWORD_RESET_CONFIRM_TEMPLATE_FILE
    success_url=reverse_lazy('accounts:login')
    form_class = NewSetPasswordForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        messages.success(self.request, _('Password has been reset'))
        return super().form_valid(form)

class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = PASSWORD_RESET_COMPLETE_TEMPLATE_FILE
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


@login_required
def profile(request):
    return render(request, VIEW_PROFILE_TEMPLATE_FILE)

@login_required
def update(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Profile has been updated'))
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
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        form = DeleteUserForm(request.POST, instance=user)
        if form.is_valid():
            user.is_active = False
            user.save()
            messages.success(request, _('User') + ' \"' + request.user.username + '\"' + _(" has been deleted"))
            logout(request)
            return redirect(settings.LOGIN_URL)
        else:
            context = {'form': form,}
            return render(request, DELETE_PROFILE_TEMPLATE_FILE, context)
    else:
        form = DeleteUserForm()
        context = {'form': form,}
        return render(request, DELETE_PROFILE_TEMPLATE_FILE, context)
            
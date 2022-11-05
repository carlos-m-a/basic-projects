from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

ERROR_MESSAGE_INCORRECT_PASSWORD = _('Incorrect password')
ERROR_MESSAGE_USERNAME_ALREADY_EXISTS = _('A user with that username already exists.')
TEXT_PASSWORD_IS_REQUIRED = _('Password is required to allow this action')

class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        label=_("Email"), 
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        label=_("Email"), 
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), 
        required=True,
        strip=False,
        label=_('Current password'), 
        help_text=TEXT_PASSWORD_IS_REQUIRED
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'current_password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() and username != self.instance.username:
            raise ValidationError(ERROR_MESSAGE_USERNAME_ALREADY_EXISTS, code='username_already_exists')
        return username

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not check_password(current_password, self.instance.password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password


class DeleteUserForm(forms.ModelForm):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), 
        required=True,
        strip=False,
        label=_('Password'), 
        help_text=TEXT_PASSWORD_IS_REQUIRED
    )

    class Meta:
        model = User
        fields = ['current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not check_password(current_password, self.instance.password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password
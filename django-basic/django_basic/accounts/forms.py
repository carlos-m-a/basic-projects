from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

ERROR_MESSAGE_INCORRECT_PASSWORD = _('Incorrect password')
TEXT_PASSWORD_IS_REQUIRED = _('Password is required to allow this action')

User = get_user_model()

class NewAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", 'placeholder':_('Enter username or email')}),
        required=True,
        strip=False,
        max_length=254,
        label=_("Username or email"),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        max_length=254,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control",'placeholder':_('Enter password')}),
    )

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return password

    def clean(self):
        return self.cleaned_data


class NewUserForm(UserCreationForm):
    username = UsernameField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", 'placeholder':_('Enter username')}),
        strip=False,
        label=_("Username"),
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        label=_("Email"), 
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class":"form-control", 'placeholder':_('Enter email')}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter password')}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter password again')}),
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class NewPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class':'form-control','placeholder':_('Enter current password')}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter new password')}),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter new password again')}),
    )

class NewPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class':'form-control', 'placeholder':_('Enter email')}),
    )

class NewSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter password')}),
        strip=False,
       
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control','placeholder':_('Enter password again')}),
    )

class UpdateUserForm(forms.ModelForm):
    username = UsernameField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", 'placeholder':_('Enter username')}),
        strip=False,
        label=_("Username"),
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        label=_("Email"), 
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class":"form-control", 'placeholder':_('Enter email')}),
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':_('Enter first name')}),
        strip=False,
        label=_("First name"),
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':_('Enter last name')}),
        strip=False,
        label=_("Last name"),
    )
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control", 'placeholder':_('Enter password')}), 
        required=True,
        strip=False,
        label=_('Password confirmation'), 
        help_text=TEXT_PASSWORD_IS_REQUIRED
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password


class DeleteUserForm(forms.ModelForm):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class":"form-control",
            'placeholder':_('Enter password')}), 
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
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password
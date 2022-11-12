from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Profile
ERROR_MESSAGE_INCORRECT_PASSWORD = _('Incorrect password')
ERROR_MESSAGE_INCORRECT_LOGIN_DATA = _('Incorrect password or username-email')
TEXT_PASSWORD_IS_REQUIRED = _('Current password is required to allow this action')

User = get_user_model()


def get_password_field(is_confirmation:bool=False, is_new:bool=False, help_text_active:bool=False):
    password_string = 'Password'
    if is_new:
        password_string = 'New ' + password_string.lower()
    placeholder_string = 'Enter ' + password_string.lower()
    placeholder_string = _(placeholder_string)
    if is_confirmation:
        password_string += ' confirmation'
    password_string = _(password_string)

    if is_confirmation and (is_new or not help_text_active):
        placeholder_string += ' again'

    password_field =  forms.CharField(
        label=password_string,
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':'form-control','placeholder':placeholder_string}),
    )
    if help_text_active:
        password_field.help_text = TEXT_PASSWORD_IS_REQUIRED
    return password_field

def get_username_field():
    return UsernameField(
            required=True,
            max_length=150,
            widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", 'placeholder':_('Enter username')}),
            strip=False,
            label=_("Username"),
        )

def get_email_field():
    return forms.EmailField(
            required=True,
            max_length=254,
            label=_("Email"), 
            widget=forms.EmailInput(attrs={"autocomplete": "email", "class":"form-control", 'placeholder':_('Enter email')}),
        )

def get_name_field(name:str):
    return forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':_('Enter ' + name.lower())}),
        strip=False,
        label=_(name.capitalize()),
    )


class NewAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class":"form-control", 'placeholder':_('Enter username or email')}),
        required=True,
        strip=False,
        max_length=254,
        label=_("Username or email"),
    )
    password = get_password_field(is_confirmation=False, is_new=False)

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
                request=self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise ValidationError(ERROR_MESSAGE_INCORRECT_LOGIN_DATA, code='invalid_login')
            else:
                self.confirm_login_allowed(self.user_cache)

        return password

    def clean(self):
        return self.cleaned_data

class NewUserForm(UserCreationForm):
    username = get_username_field()
    email = get_email_field()
    password1 = get_password_field(is_confirmation=False, is_new=False)
    password2 = get_password_field(is_confirmation=True, is_new=False)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class NewPasswordChangeForm(PasswordChangeForm):
    old_password = get_password_field(is_confirmation=True, is_new=False, help_text_active=True)
    new_password1 = get_password_field(is_confirmation=False, is_new=True)
    new_password2 = get_password_field(is_confirmation=True, is_new=True)

class NewPasswordResetForm(PasswordResetForm):
    email = get_email_field()

class NewSetPasswordForm(SetPasswordForm):
    new_password1 = get_password_field(is_confirmation=False, is_new=True)
    new_password2 = get_password_field(is_confirmation=True, is_new=True)

class UpdateUserForm(forms.ModelForm):
    username = get_username_field()
    first_name = get_name_field('first name')
    last_name = get_name_field('last name')
    current_password = get_password_field(is_confirmation=True, is_new=False, help_text_active=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password

class DeleteUserForm(forms.ModelForm):
    current_password = get_password_field(is_confirmation=True, is_new=False, help_text_active=True)

    class Meta:
        model = User
        fields = ['current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password

class UpdateEmailForm(forms.ModelForm):
    email = get_email_field()
    current_password = get_password_field(is_confirmation=True, is_new=False, help_text_active=True)
    class Meta:
        model = User
        fields = ['email','current_password']
    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password

class UpdateProfileForm(forms.ModelForm):
    bio_text = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.Textarea(attrs={"class":"form-control", 'rows':"3", 'placeholder':_('Enter short biography')}),
        strip=False,
        label=_('Biography'),
    )
    date_of_birth = forms.DateField(
        required=False,
        label=_("Date of birth"), 
        widget= forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'required': False, })
    )
    class Meta:
        model = Profile
        fields = ['bio_text', 'date_of_birth']

class UpdateProfileImageForm(forms.ModelForm):
    avatar_image = forms.FileField(
        required=False,
        max_length=254,
        label=_("Logo image"), 
        widget= forms.FileInput(attrs={'class':'form-control', 'required': False, })
    )
    
    class Meta:
        model = Profile
        fields = ['avatar_image']
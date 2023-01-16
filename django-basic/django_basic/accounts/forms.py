from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Profile

ERROR_MESSAGE_INCORRECT_PASSWORD = _('Incorrect password')
ERROR_MESSAGE_INCORRECT_LOGIN_DATA = _('Incorrect password or username-email')
TEXT_PASSWORD_IS_REQUIRED = _('Current password is required to allow this action')

INPUT_FIELD_HTML_CLASS = "form-control"

User = get_user_model()



#####################################
### Field definition forms ##########
#####################################


class NewPasswordFieldsForm(forms.Form):
    new_password1 = forms.CharField(
        label=_('New password'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_('Enter new password'),}),
    )
    new_password2 = forms.CharField(
        label=_('New password confirmation'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_('Enter new password again'),}),
    )

class CurrentPasswordFieldForm(forms.Form):
    current_password =  forms.CharField(
        label=_('Password confirmation'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_("Enter password")}),
        help_text = TEXT_PASSWORD_IS_REQUIRED
    )

class UsernameFieldForm(forms.Form):
    username = UsernameField(
            required=True,
            max_length=150,
            widget=forms.TextInput(attrs={"autofocus": True, "class":INPUT_FIELD_HTML_CLASS, 'placeholder':_('Enter username')}),
            strip=False,
            label=_("Username"),
        )

class EmailFieldForm(forms.Form):
    email = forms.EmailField(
            required=True,
            max_length=254,
            label=_("Email"), 
            widget=forms.EmailInput(attrs={"autocomplete": "email", "class":INPUT_FIELD_HTML_CLASS, 'placeholder':_('Enter email')}),
        )

class NamesFieldsForm(forms.Form):
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class":INPUT_FIELD_HTML_CLASS, 'placeholder':_('Enter first name')}),
        strip=False,
        label=_('First name'),
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class":INPUT_FIELD_HTML_CLASS, 'placeholder':_('Enter last name')}),
        strip=False,
        label=_('Last name'),
    )



#####################################
###########  New forms  #############
#####################################

class NewAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class":INPUT_FIELD_HTML_CLASS, 'placeholder':_('Enter username or email')}),
        required=True,
        strip=False,
        max_length=254,
        label=_("Username or email"),
    )
    password = forms.CharField(
        label=_('Password'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_('Enter password'),}),
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
                request=self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise ValidationError(ERROR_MESSAGE_INCORRECT_LOGIN_DATA, code='invalid_login')
            else:
                self.confirm_login_allowed(self.user_cache)

        return password

    def clean(self):
        return self.cleaned_data

class NewUserForm(UsernameFieldForm, EmailFieldForm, UserCreationForm):
    password1 = forms.CharField(
        label=_('Password'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_('Enter password'),}),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_('Enter password again'),}),
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class NewPasswordChangeForm(NewPasswordFieldsForm, PasswordChangeForm):
    old_password =  forms.CharField(
        label=_('Password confirmation'),
        required=True,
        strip=False,
        max_length=150,
        widget=forms.PasswordInput(attrs={"autocomplete": "on password", 'class':INPUT_FIELD_HTML_CLASS,'placeholder':_("Enter password")}),
        help_text = TEXT_PASSWORD_IS_REQUIRED
    )

class NewPasswordResetForm(EmailFieldForm, PasswordResetForm):
    pass

class NewSetPasswordForm(NewPasswordFieldsForm, SetPasswordForm):
    pass

class UpdateUserForm(UsernameFieldForm, NamesFieldsForm, CurrentPasswordFieldForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password

class DeleteUserForm(CurrentPasswordFieldForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['current_password']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError(ERROR_MESSAGE_INCORRECT_PASSWORD, code='password_invalid')
        return current_password

class UpdateEmailForm(EmailFieldForm, CurrentPasswordFieldForm, forms.ModelForm):
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
        widget=forms.Textarea(attrs={"class":INPUT_FIELD_HTML_CLASS, 'rows':"3", 'placeholder':_('Enter short biography')}),
        strip=False,
        label=_('Biography'),
    )
    date_of_birth = forms.DateField(
        required=False,
        label=_("Date of birth"), 
        widget= forms.DateInput(attrs={'type': 'date', 'class':INPUT_FIELD_HTML_CLASS, 'required': False, })
    )
    class Meta:
        model = Profile
        fields = ['bio_text', 'date_of_birth']

class UpdateProfileImageForm(forms.ModelForm):
    avatar_image = forms.ImageField(
        required=False,
        max_length=254,
        label=_("Logo image"), 
        widget= forms.FileInput(attrs={'class':INPUT_FIELD_HTML_CLASS, 'required': False, })
    )
    
    class Meta:
        model = Profile
        fields = ['avatar_image']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    current_password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'current_password']

    def clean(self):
        username = self.cleaned_data['username']
        current_password = self.cleaned_data['current_password']

        if User.objects.filter(username=username).exists() and username != self.instance.username:
            self.add_error('username','This username already exists')
        if not check_password(current_password, self.instance.password):
            self.add_error('current_password', 'Incorrect password')

class DeleteUserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
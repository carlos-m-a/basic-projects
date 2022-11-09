from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from . import forms

User = get_user_model()

RANDOM_EMAIL_255_LENGTH = 'aaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaa@mail.com'
RANDOM_STRING_151_LENGTH = 'aaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWaaaaaaaaaWa'


class RegistrationFormTestCase(TestCase):

    def test_success_case(self):
        data = {'username':'user3', 'email':'user3@mail.com', 'password1':'jajajeje11', 'password2':'jajajeje11'}
        form = forms.NewUserForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)
        user = form.save()
        self.assertEqual(user.username, 'user3')
        self.assertEqual(user.email, 'user3@mail.com')
        self.assertTrue(check_password('jajajeje11', user.password))

    def test_registration_empty_fields(self):
        form = forms.NewUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])
        self.assertEqual(len(form.errors), 4)

        data = {'username':'', 'email':'', 'password1':'', 'password2':''}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])
        self.assertEqual(len(form.errors), 4)

    def test_max_length_fields(self):
        data = {'username':RANDOM_STRING_151_LENGTH, 'email': RANDOM_EMAIL_255_LENGTH,
            'password1': 'jajajeje11', 'password2':'jajajeje11',}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Ensure this value has at most 254 characters (it has 255).'])
        self.assertEqual(form.errors['username'], ['Ensure this value has at most 150 characters (it has 151).'])
        self.assertEqual(len(form.errors), 2)

    def test_username_already_in_use(self):
        user2 = User()
        user2.username = 'user2'
        user2.email = 'user2@mail.com'
        user2.set_password('jajajeje22')
        user2.save()
        data = {'username':'user2', 'email':'user1@mail.com', 'password1':'asdffdsa1', 'password2':'asdffdsa1'}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])
        self.assertEqual(len(form.errors), 1)

    def test_incorrect_email(self):
        data = {'username':'user1', 'email':'user1@mail.', 'password1':'asdffdsa1', 'password2':'asdffdsa1'}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

        data = {'username':'user1', 'email':'user1@.com', 'password1':'asdffdsa1', 'password2':'asdffdsa1'}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

        data = {'username':'user1', 'email':'usér1@mail.com', 'password1':'asdffdsa1', 'password2':'asdffdsa1'}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

    def test_incorrect_username(self):
        data = {'username':'user3%', 'email':'user1@mail.com', 'password1':'asdffdsa1', 'password2':'asdffdsa1'}
        form = forms.NewUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'])
        self.assertEqual(len(form.errors), 1)


class UpdateUserFormTestCase(TestCase):

    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user

    def test_success_case(self):
        data = {'username':'user3', 'email':'user3@mail.com', 'current_password':'jajajeje11', 'first_name':'Name3', 'last_name':'Surname3'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)
        user = form.save()
        self.assertEqual(user.username, 'user3')
        self.assertEqual(user.email, 'user3@mail.com')
        self.assertEqual(user.first_name, 'Name3')
        self.assertEqual(user.last_name, 'Surname3')

    def test_empty_fields(self):
        form = forms.UpdateUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['current_password'], ['This field is required.'])
        self.assertEqual(len(form.errors), 3)

        data = {'username':'', 'email':'', 'current_password':''}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['current_password'], ['This field is required.'])
        self.assertEqual(len(form.errors), 3)
    
    def test_max_length_fields(self):
        data = {'username':RANDOM_STRING_151_LENGTH, 'email': RANDOM_EMAIL_255_LENGTH,
            'current_password': 'jajajeje11', 'first_name':RANDOM_STRING_151_LENGTH,
            'last_name': RANDOM_STRING_151_LENGTH}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Ensure this value has at most 254 characters (it has 255).'])
        self.assertEqual(form.errors['username'], ['Ensure this value has at most 150 characters (it has 151).'])
        self.assertEqual(form.errors['first_name'], ['Ensure this value has at most 150 characters (it has 151).'])
        self.assertEqual(form.errors['last_name'], ['Ensure this value has at most 150 characters (it has 151).'])
        self.assertEqual(len(form.errors), 4)

    def test_wrong_password(self):
        data = {'username':'user1', 'email':'user1@mail.com', 'current_password':'IncorrectPassword'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['current_password'], [forms.ERROR_MESSAGE_INCORRECT_PASSWORD])
        self.assertEqual(len(form.errors), 1)

    def test_username_already_in_use(self):
        user2 = User()
        user2.username = 'user2'
        user2.email = 'user2@mail.com'
        user2.set_password('jajajeje22')
        user2.save()
        data = {'username':'user2', 'email':'user1@mail.com', 'current_password':'jajajeje11'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])
        self.assertEqual(len(form.errors), 1)

    def test_incorrect_email(self):
        data = {'username':'user1', 'email':'user1@mail.', 'current_password':'jajajeje11'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

        data = {'username':'user1', 'email':'user1@.com', 'current_password':'jajajeje11'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

        data = {'username':'user1', 'email':'usér1@mail.com', 'current_password':'jajajeje11'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(len(form.errors), 1)

    def test_incorrect_username(self):
        data = {'username':'user3%', 'email':'user1@mail.com', 'current_password':'jajajeje11'}
        form = forms.UpdateUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'])
        self.assertEqual(len(form.errors), 1)


class DeleteUserFormTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user

    def test_success_case(self):
        data = {'current_password':'jajajeje11'}
        form = forms.DeleteUserForm(data=data, instance=self.user)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_empty_fields(self):
        form = forms.DeleteUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['current_password'], ['This field is required.'])
        self.assertEqual(len(form.errors), 1)

        data = {'current_password':''}
        form = forms.DeleteUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['current_password'], ['This field is required.'])
        self.assertEqual(len(form.errors), 1)

    def test_wrong_password(self):
        data = {'current_password':'IncorrectPassword'}
        form = forms.DeleteUserForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['current_password'], [forms.ERROR_MESSAGE_INCORRECT_PASSWORD])
        self.assertEqual(len(form.errors), 1)


class NewAuthenticationFormTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user:User = user

    def test_success_case(self):
        data = {'username':'user1', 'password':'jajajeje11'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)
        
        data = {'username':'user1@mail.com', 'password':'jajajeje11'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_empty_fields(self):
        form = forms.NewAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        
        data = {'username':'', 'password':''}
        form = forms.NewAuthenticationForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertEqual(len(form.errors), 2)
    
    def test_max_length_fields(self):
        data = {'username':RANDOM_EMAIL_255_LENGTH, 'password': RANDOM_STRING_151_LENGTH}
        form = forms.NewAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['Ensure this value has at most 254 characters (it has 255).'])
        self.assertEqual(form.errors['password'], ['Ensure this value has at most 150 characters (it has 151).'])
        self.assertEqual(len(form.errors), 2)

    def test_wrong_password(self):
        data = {'username':'user1', 'password':'IncorrectPassword'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [forms.ERROR_MESSAGE_INCORRECT_LOGIN_DATA])
        self.assertEqual(len(form.errors), 1)

    def test_non_existent_username(self):
        data = {'username':'user3', 'password':'jajajeje11'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [forms.ERROR_MESSAGE_INCORRECT_LOGIN_DATA])
        self.assertEqual(len(form.errors), 1)

    def test_non_existent_email(self):
        data = {'username':'user3@mail.com', 'password':'jajajeje11'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [forms.ERROR_MESSAGE_INCORRECT_LOGIN_DATA])
        self.assertEqual(len(form.errors), 1)

    def test_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        data = {'username':'user1', 'password':'jajajeje11'}
        form = forms.NewAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [forms.ERROR_MESSAGE_INCORRECT_LOGIN_DATA])
        self.assertEqual(len(form.errors), 1)
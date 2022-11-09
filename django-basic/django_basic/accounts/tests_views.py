from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.http import urlencode
from http import HTTPStatus
from . import views
from . import forms

User = get_user_model()


class NonAllowedRequestsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()

    def test_non_allowed_requests_for_authenticated_user(self):
        self.client.login(username='user1', password='jajajeje11')
        response = self.client.get(reverse('accounts:register'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:login'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:password_reset'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:password_reset_done'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:password_reset_confirm', kwargs={'uidb64':'A7A', 'token':'adf867sajdffJK'}), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:password_reset_complete'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:register'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:login'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:password_reset'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:password_reset_done'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:password_reset_confirm', kwargs={'uidb64':'A7A', 'token':'adf867sajdffJK'}), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.post(reverse('accounts:password_reset_complete'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        response = self.client.get(reverse('accounts:logout'), follow=True)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)

    def test_non_allowed_requests_for_non_authenticated_user(self):
        response = self.client.get(reverse('accounts:password_change'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/password_change/' }))
        response = self.client.get(reverse('accounts:password_change_done'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/password_change_done/' }))
        response = self.client.get(reverse('accounts:profile'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/profile/' }))
        response = self.client.get(reverse('accounts:update'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/update/' }))
        response = self.client.get(reverse('accounts:delete'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/delete/' }))
        response = self.client.post(reverse('accounts:password_change'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/password_change/' }))
        response = self.client.post(reverse('accounts:password_change_done'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/password_change_done/' }))
        response = self.client.post(reverse('accounts:profile'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/profile/' }))
        response = self.client.post(reverse('accounts:update'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/update/' }))
        response = self.client.post(reverse('accounts:delete'))
        self.assertRedirects(response, reverse('accounts:login') + '?' + urlencode({'next': '/accounts/delete/' }))


class ViewProfileTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user
        self.client.login(username='user1', password='jajajeje11')

    def test_load(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.VIEW_PROFILE_TEMPLATE_FILE)
        self.assertEqual


class UpdateProfileTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user
        self.client.login(username='user1', password='jajajeje11')

    def test_load(self):
        response = self.client.get(reverse('accounts:update'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.UPDATE_PROFILE_TEMPLATE_FILE)
        self.assertEqual(self.user.username, response.context['user'].username)

    def test_invalid_data(self):
        data={'email':'', 'current_password':'incorrectpassword'}
        response = self.client.post(reverse('accounts:update'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.UPDATE_PROFILE_TEMPLATE_FILE)
        self.assertEqual(self.user.username, response.context['user'].username)
        self.assertEqual(type(response.context['form']), forms.UpdateUserForm)
        self.assertEqual(len(response.context['form'].errors), 3)
    
    def test_valid_data(self):
        data={'username':'user3', 'email':'user3@mail.com', 'first_name':'name3', 'current_password':'jajajeje11'}
        response = self.client.post(reverse('accounts:update'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:profile'))
        self.assertEqual(User.objects.filter(username='user3').count(), 1)
        self.assertEqual(User.objects.filter(username='user1').count(), 0)
        self.assertEqual(User.objects.get(username='user3').email, 'user3@mail.com')


class DeleteProfileTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user
        self.client.login(username='user1', password='jajajeje11')

    def test_load(self):
        response = self.client.get(reverse('accounts:delete'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.DELETE_PROFILE_TEMPLATE_FILE)
        self.assertEqual(self.user.username, response.context['user'].username)

    def test_invalid_data(self):
        data={'current_password':'incorrectpassword'}
        response = self.client.post(reverse('accounts:delete'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.DELETE_PROFILE_TEMPLATE_FILE)
        self.assertEqual(self.user.username, response.context['user'].username)
        self.assertEqual(type(response.context['form']), forms.DeleteUserForm)
        self.assertEqual(len(response.context['form'].errors), 1)


    def test_valid_data(self):
        data={'current_password':'jajajeje11'}
        response = self.client.post(reverse('accounts:delete'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login'))
        self.assertEqual(User.objects.filter(username='user1').count(), 1)
        self.assertEqual(User.objects.get(username='user1').is_active, False)
    

class RegisterTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user

    def test_load(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.REGISTER_USER_TEMPLATE_FILE)

    def test_invalid_data(self):
        data={'email':'', 'password1':'jajajeje1', 'password2':'jajajeje2'}
        response = self.client.post(reverse('accounts:register'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(type(response.context['form']), forms.NewUserForm)
        self.assertTemplateUsed(response, views.REGISTER_USER_TEMPLATE_FILE)
        self.assertEqual(len(response.context['form'].errors), 3)
    
    def test_valid_data(self):
        data={'username':'user3', 'email':'user3@mail.com', 'first_name':'name3', 'password1':'jajajeje3', 'password2':'jajajeje3'}
        response = self.client.post(reverse('accounts:register'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.REGISTER_USER_DONE_TEMPLATE_FILE)
        self.assertEqual(User.objects.filter(username='user3').count(), 1)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(User.objects.get(username='user3').email, 'user3@mail.com')


class LoginTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user
        # self.client.login(username='user1', password='jajajeje11')

    def test_load(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.LOGIN_TEMPLATE_FILE)

    def test_invalid_data(self):
        data={'username':'user1', 'password':'incorrectpassword'}
        response = self.client.post(reverse('accounts:login'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, views.LOGIN_TEMPLATE_FILE)
        self.assertEqual(response.context['form'].cleaned_data['username'], 'user1')
        self.assertEqual(type(response.context['form']), forms.NewAuthenticationForm)
        self.assertEqual(len(response.context['form'].errors), 1)
        #to check if user is NOT logged in
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_valid_data(self):
        data={'username':'user1', 'password':'jajajeje11'}
        response = self.client.post(reverse('accounts:login'), data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        #to check if user is logged in
        response = self.client.get(reverse('accounts:login'))
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)


class LogoutTestCase(TestCase):
    
    def setUp(self):
        user = User()
        user.username = 'user1'
        user.email = 'user1@mail.com'
        user.set_password('jajajeje11')
        user.save()
        self.user = user
        self.client.login(username='user1', password='jajajeje11')

    def test_valid_logout(self):
        response = self.client.post(reverse('accounts:logout'), data={})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, settings.LOGOUT_REDIRECT_URL)
         #to check if user is NOT logged in
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
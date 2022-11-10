from django.test import TestCase
from django.urls import reverse

class RegistrationFormTestCase(TestCase):

    def test_urls(self):
        url = reverse('accounts:register')
        self.assertEqual(url, '/accounts/register/')

        url = reverse('accounts:login')
        self.assertEqual(url, '/accounts/login/')

        url = reverse('accounts:logout')
        self.assertEqual(url, '/accounts/logout/')

        url = reverse('accounts:password_change')
        self.assertEqual(url, '/accounts/password_change/')

        url = reverse('accounts:password_change_done')
        self.assertEqual(url, '/accounts/password_change_done/')

        url = reverse('accounts:password_reset')
        self.assertEqual(url, '/accounts/password_reset/')

        url = reverse('accounts:password_reset_confirm', kwargs={'uidb64':'A7A', 'token':'adf867sajdffJK'})
        self.assertEqual(url, '/accounts/reset/A7A/adf867sajdffJK/')

        url = reverse('accounts:password_reset_complete')
        self.assertEqual(url, '/accounts/reset/')

        url = reverse('accounts:update')
        self.assertEqual(url, '/accounts/update/')

        url = reverse('accounts:delete')
        self.assertEqual(url, '/accounts/delete/')

        url = reverse('accounts:profile')
        self.assertEqual(url, '/accounts/profile/')

        url = reverse('accounts:update_profile')
        self.assertEqual(url, '/accounts/profile/update/')

        url = reverse('accounts:update_email')
        self.assertEqual(url, '/accounts/update_email/')
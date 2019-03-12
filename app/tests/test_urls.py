from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse


class test_accounts_page(TestCase):
    def setUp(self):
        self.client = Client()

    def test_getLogin(self):
        response = self.client.get("http://127.0.0.1:8000/accounts/login/")
        assert response.status_code == 200

    def test_landing_redirect(self):
        response = self.client.get("http://127.0.0.1:8000", follow=True)
        SimpleTestCase().assertRedirects(response, "/accounts/login/?next=/")

    def test_signup_button(self):
        response = self.client.get("http://127.0.0.1:8000/accounts/login/")


class test_signup_page(TestCase):
    def setUP(self):
        self.client = Client()

    def test_getSignUp(self):
        response = self.client.get("http://127.0.0.1:8000/accounts/signup/")
        assert response.status_code == 200

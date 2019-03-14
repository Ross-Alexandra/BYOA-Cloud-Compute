from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse


class TestAccountsPage(TestCase):
    def test_getLogin(self):
        client = Client()
        response = self.client.get("http://127.0.0.1:8000/accounts/login/")
        assert response.status_code == 200

    def test_landing_redirect(self):
        client = Client()
        response = self.client.get("http://127.0.0.1:8000", follow=True)
        SimpleTestCase().assertRedirects(response, "/accounts/login/?next=/")


class test_signup_page(TestCase):
    def test_get_signup(self):
        client = Client()
        response = client.get("http://127.0.0.1:8000/accounts/signup/")
        assert response.status_code == 200

    def test_get_signup_by_name(self):
        client = Client()
        response = client.get(reverse("signup"))
        assert response.status_code == 200

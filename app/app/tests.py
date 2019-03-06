import pytest
from django.test import Client, TestCase
from django.urls import reverse


class test_Accounts(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_getLogin(self):
        client = Client()
        response = client.get("http://127.0.0.1:8000/accounts/login/")
        self.assertEqual(response.status_code, 200)

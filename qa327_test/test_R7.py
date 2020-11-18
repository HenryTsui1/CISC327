import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('Test!!')
)

class R7Test(BaseCase):



    #R7.1 Logout will invalid the current session and redirect to the login page. 
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R7_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test@test.com')
        self.type("#password", 'Test!!')
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")
        self.open(base_url + '/logout')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    #R7.2 After logout, the user shouldn't be able to access restricted pages.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R7_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test@test.com')
        self.type("#password", 'Test!!')
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")
        self.open(base_url + '/logout')
        self.open(base_url + '/')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

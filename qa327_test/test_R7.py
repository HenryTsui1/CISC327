import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

class R1Test(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @login_required
    #R7.1 Logout will invalid the current session and redirect to the login page. 
    def test_R7_1(self, *_):
        self.open(base_url + '/login')
        self.type("#email", test_user[0])
        self.type("#password", test_user[2])
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.assert_text("Log In", "#login-header")

    #R7.2 After logout, the user shouldn't be able to access restricted pages.
    def test_R7_2(self, *_):
        self.open(base_url + '/login')
        self.type("#email", test_user[0])
        self.type("#password", test_user[2])
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.open(base_url + '/')
        self.assert_text("Log In", "#login-header")
        self.open(base_url + '/buy')
        self.assert_text("Log In", "#login-header")
        self.open(base_url + '/sell')
        self.assert_text("Log In", "#login-header")
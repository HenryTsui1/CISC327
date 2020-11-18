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

class R8Test(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    @login_required

    #R8.1 When opening any other page that does not exist, check for 404 message.
    def test_R8_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/*') #any other page name that does not exist
        self.assert_element("Error 404 - Page not found.", "#welcome-header")


    #R8.2 Make sure that GET and POST work on /register, and verify that error 404 is displayed
    def test_R8_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test_frontend@test.com')
        self.type("#password", 'test_frontend')
        self.click('input[type="submit"]') #Can not direct to /register
        self.assert_text("Error 404 - Page not found", "#welcome-header") #redircts to the error404 page

    #R8.3 Make sure that GET and POST work on /register, and verify that error 404 is displayed
    def test_R8_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")
        self.click('input[type="submit"]')
        self.assert_text("Error 404 - Page not found", "#welcome-header")

    #R8.4 Make sure that only GET works on /, and verify that error 404 is displayed
    def test_R8_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test_frontend@test.com')
        self.type("#password", 'test_frontend')
        self.click('input[type="submit"]')
        self.assert_text("Error 404 - Page not found", "#welcome-header")

    #R8.5 Make sure that only GET and POST work on /logout
    def test_R8_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test_frontend@test.com')
        self.type("#password", 'test_frontend')
        self.click('input[type="submit"]')
        self.clic('input[type="logout"]')
        self.assert_text("Error 404 - Page not found", "#welcome-header") #does not direct to /logout, error 404

    #R8.6 Make sure that only POST works on /buy
    def test_R8_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test_frontend@test.com')
        self.type("#password", 'test_frontend')
        self.click('input[type="submit"]')
        self.assert_text("Error 404 - Page not found", "#welcome-header") #Can not access /buy via "/", directs to error 404 page

    #R8.7 Make sure that only POST works on /sell
    def test_R8_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", 'test_frontend@test.com')
        self.type("#password", 'test_frontend')
        self.click('input[type="submit"]')
        self.assert_text("Error 404 - Page not found", "#welcome-header") #Can not access /sell via "/", directs to error 404 page

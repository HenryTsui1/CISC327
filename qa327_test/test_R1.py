import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
Test case for R1 requirements.
"""

# Moch a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('Test!!')
)


class R1Test(BaseCase):

    # Test Case R1.1 If the user hasn't logged in, show the login page.
    def test_R1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    # Test Case R1.2 The login page has a message that by default says 'please login'.
    def test_R1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#message")
        self.assert_text("Please Login", "#message")

    # Test case R1.3 - If the user has logged in, redirect to the user profile page.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.4 - The login page provides a login form which requests two fields: email and password.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")
        
    # Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login).
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.6.1 - Email and password both cannot be empty. - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_6_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.6.2 - Email and password both cannot be empty. - Negative (password is empty)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_6_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.click('input[type="submit"]')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    # Test case R1.6.3 - Email and password both cannot be empty. - Negative (username is empty)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_6_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")

    # Test case R1.7.1 - Email has to follow addr-spec defined in RFC 5322. -Postive
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_7_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.7.2 - Email has to follow addr-spec defined in RFC 5322. -Negative (doesn't follow addr-spec defined)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_7_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "asjdh")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.8.1 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Postive
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_8_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.8.2 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (less than 6 characters)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_8_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.8.3 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no upper case letter)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_8_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "test!!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.8.4 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no lower case letter)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_8_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "TEST!!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.8.5 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no special character)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_8_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Testtt")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_9(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "haskjfh")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password format is incorrect." , "#message")

    # Test case R1.10 - If email/password are correct, redirect to /.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_10(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi" , "#welcome-header")

    # Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_11(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!!!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email/password combination incorrect." , "#message")

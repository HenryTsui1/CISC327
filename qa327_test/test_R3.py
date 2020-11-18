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

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]

class R3Test(BaseCase):

# # R3.1 If the user is not logged in, redirect to login page
#     def test_R3_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.assert_element("#login-header")
#         self.assert_text("Log In", "#login-header")

# # R3.2 This page shows a header 'Hi {}'.format(user.name)
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R3_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]')
#         self.assert_element("#welcome-header")
#         self.assert_text("Hi " + test_user.name + " !" , "#welcome-header")

# # R3.3 This page shows user balance.
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R3_3(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]')
#         self.assert_element("#balance-elem")
#         self.assert_text("Balance" , "#balance-elem")

# # R3.4 This page shows a logout link, pointing to /logout
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R3_4(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]')        
#         self.assert_element("#logout")
#         self.click('#logout')
#         self.assert_element("#login-header")
#         self.assert_text("Log In", "#login-header")

# # R3.5 This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
#     @patch('qa327.backend.get_user', return_value=test_user)
#     @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
#     def test_R3_5(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]') 
#         self.assert_element("#tickets div h4")
#         self.assert_text("t1 100", "#tickets div h4")

# # R3.6 This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R3_6(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]')
#         self.assert_element("#sell-form")
#         self.assert_element("#sell-name")
#         self.assert_element("#sell-quantity")
#         self.assert_element("#sell-price")
#         self.assert_element("#sell-exp")

# # R3.7 This page contains a form that a user can buy new tickets. Fields: name, quantity
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R3_7(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test@test.com")
#         self.type("#password", "Test!!")
#         self.click('input[type="submit"]')
#         self.assert_element("#buy-form")
#         self.assert_element("#buy-name")
#         self.assert_element("#buy-quantity")

# R3.8 This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R3_8(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#upd-form")
        self.assert_element("#upd-name")
        self.assert_element("#upd-quantity")
        self.assert_element("#upd-price")
        self.assert_element("#upd-exp")

# R3.9 The ticket-selling form can be posted to /sell
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R3_9(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#sell-form")
        self.type("#sell-name", "Test")
        self.type("#sell-quantity", "5")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12/12/2020")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")

# R3.10 The ticket-buying form can be posted to /buy
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R3_10(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#buy-form")
        self.type("#buy-name", "Test")
        self.type("#buy-quantity", "5")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# R3.11 The ticket-update form can be posted to /update
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R3_11(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.assert_element("#upd-form")
        self.type("#upd-name", "Test")
        self.type("#upd-quantity", "5")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12/12/2020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")


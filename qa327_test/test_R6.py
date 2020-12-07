import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('Test!!'),
    balance = 5000
)
# Moch a poor sample user
test_user_poor = User(
    email='test_poor@test.com',
    name='test_user_poor',
    password=generate_password_hash('Test!!'),
    balance = 1
)
# Moch some sample tickets
test_tickets = Ticket(
    title='TestTest',
    quantity=80,
    price=50,
    expDate=20201212
)


class R5Test(BaseCase):
# Test Case R6.1.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# Test Case R6.1.2 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Non-Aplhanumeric)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest$$")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Name Format Error", "#bMessage")

# Test Case R6.1.3 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in first character)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", " TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Name Format Error", "#bMessage")

# Test Case R6.1.4 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in last character)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_1_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest ")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Name Format Error", "#bMessage")

# Test Case R6.2.1 The name of the ticket is no longer than 60 characters. - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_2_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# Test Case R6.2.2 The name of the ticket is no longer than 60 characters. - Negative
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_2_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Name Format Error", "#bMessage")

# Test Case R6.3.1 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# Test Case R6.3.2 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantity of 0)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_3_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "0")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Invalid Quantity", "#bMessage")

# Test Case R6.3.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantity of 101)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_3_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "101")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Invalid Quantity", "#bMessage")

# Test Case R6.4.1 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# Test Case R6.4.2 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Negative (Ticket name does not exist in the database)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R6_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "asdfghj")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Ticket Does Not Exist", "#bMessage")

# Test Case R6.4.3 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Negative (Quantity is less than quantity requested to buy)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_4_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "81")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Not Enough Tickets Left", "#bMessage")

# Test Case R6.5.1 The user has more balance than the ticket price * quantity + service fee(35%) + tax(5%) - Positive
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_5_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#message")
        self.assert_text("Bought", "#message")

# Test Case R6.5.2 The user has more balance than the ticket price * quantity + service fee(35%) + tax(5%) - Negative (Balance less than ticket price * quantity + service fee(35%) + tax(5%)
    @patch('qa327.backend.get_user', return_value=test_user_poor)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R6_5_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_poor@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Insufficient Funds", "#bMessage")

# Test Case R6.6 For any errors, redirect back to / and show an error message
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R6_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#buy-name", "TestTest2")
        self.type("#buy-quantity", "10")
        self.click('input[id="buy-submit"]')
        self.assert_element("#bMessage")
        self.assert_text("Ticket Does Not Exist", "#bMessage")

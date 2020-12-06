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
# Moch some sample tickets
test_tickets = Ticket(
    title='TestTest',
    quantity=50,
    price=50,
    expDate=20201212
)


class R5Test(BaseCase):
# The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(Positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")

# #The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(negative - non-alphanumeric)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "@!@#$%^&")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Name Format Error", "#uMessage")


# # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(negative - space front, and space back)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "frontSpace ")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Name Format Error", "#uMessage")

        self.type("#upd-name", " backSpace")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Name Format Error", "#uMessage")


# # 	The name of the ticket is no longer than 60 characters (Positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_1_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")


# # 	The name of the ticket is no longer than 60 characters (Negative)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_1_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTestaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Name Format Error", "#uMessage")



# # The quantity of the tickets has to be more than 0, and less than or equal to 100.(positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_2_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")


# The quantity of the tickets has to be more than 0, and less than or equal to 100.(negative - below and above range)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_2_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "-2")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Quantity", "#uMessage")

        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "101")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Quantity", "#uMessage")


# # Price has to be of range [10, 100] (positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")


# # Price has to be of range [10, 100] (negative)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "5")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Price", "#uMessage")

        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "101")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Price", "#uMessage")


# # Date must be given in the format YYYYMMDD (e.g. 20200901) (positive, only check that its an int of length 8)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122020")
        self.click('input[id="upd-submit"]')
        self.assert_element("#message")
        self.assert_text("Updated", "#message")


# Date must be given in the format YYYYMMDD (e.g. 20200901) (negative, only check that its an int of length 8)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122022020200")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Date Format (YYYYMMDD)", "#uMessage")




# For any errors, redirect back to / and show an error message
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
       

        self.type("#upd-name", "TestTest@!@!@!@")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12121212")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Name Format Error", "#uMessage")

        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "1000000")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12345678")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Quantity", "#uMessage")


        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "15")
        self.type("#upd-price", "-2")
        self.type("#upd-exp", "12345678")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Price", "#uMessage")

        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "10")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12122022020200")
        self.click('input[id="upd-submit"]')
        self.assert_element("#uMessage")
        self.assert_text("Invalid Date Format (YYYYMMDD)", "#uMessage")




#	The ticket of the given name must exist (positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R5_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')

        self.type("#upd-name", "TestTest")
        self.type("#upd-quantity", "20")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12345678")
        self.click('input[id="upd-submit"]')


#	The ticket of the given name must exist (negative)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R5_7(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')

        self.type("#upd-name", "randomRandomRandom")
        self.type("#upd-quantity", "20")
        self.type("#upd-price", "10")
        self.type("#upd-exp", "12345678")
        self.click('input[id="upd-submit"]')

        self.assert_element("#uMessage")
        self.assert_text("Ticket Does Not Exist", "#uMessage")



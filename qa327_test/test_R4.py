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


class R4Test(BaseCase):
# The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(Positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")

# #The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(negative - non-alphanumeric)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "@!@#$%^&")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Name Format Error", "#sMessage")


# # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.(negative - space front, and space back)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "frontSpace ")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Name Format Error", "#sMessage")

        self.type("#sell-name", " backSpace")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Name Format Error", "#sMessage")


# # 	The name of the ticket is no longer than 60 characters (Positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_1_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")


# # 	The name of the ticket is no longer than 60 characters (Negative)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_1_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTestaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Name Format Error", "#sMessage")



# # The quantity of the tickets has to be more than 0, and less than or equal to 100.(positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_2_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")


# The quantity of the tickets has to be more than 0, and less than or equal to 100.(negative - below and above range)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_2_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "-2")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Quantity", "#sMessage")

        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "101")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Quantity", "#sMessage")


# # Price has to be of range [10, 100] (positive)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")


# # Price has to be of range [10, 100] (negative)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "5")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Price", "#sMessage")

        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "101")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Price", "#sMessage")


# # Date must be given in the format YYYYMMDD (e.g. 20200901) (positive, only check that its an int of length 8)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.assert_element("#message")
        self.assert_text("Sold", "#message")


# Date must be given in the format YYYYMMDD (e.g. 20200901) (negative, only check that its an int of length 8)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122022020200")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Date Format (YYYYMMDD)", "#sMessage")




# For any errors, redirect back to / and show an error message
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R4_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
       

        self.type("#sell-name", "TestTest@!@!@!@")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12121212")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Name Format Error", "#sMessage")

        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "1000000")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12345678")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Quantity", "#sMessage")


        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "15")
        self.type("#sell-price", "-2")
        self.type("#sell-exp", "12345678")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Price", "#sMessage")

        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "10")
        self.type("#sell-exp", "12122022020200")
        self.click('input[id="sell-submit"]')
        self.assert_element("#sMessage")
        self.assert_text("Invalid Date Format (YYYYMMDD)", "#sMessage")




# The added new ticket information will be posted on the user profile page
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_tickets)
    def test_R4_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test.com")
        self.type("#password", "Test!!")
        self.click('input[type="submit"]')
# ticket already spoofed
        self.click('input[type = "submit"]')
        self.assert_element("#tickets")
        self.assert_text("TestTest", "#tickets")



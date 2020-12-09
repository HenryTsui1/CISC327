import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch


class IntegrationTest(BaseCase):

    # Test posting
    def test_integration_posting(self, *_):
        #register
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "test01@test.com")
        self.type("#name", "int testing")
        self.type("#password", "Test!!")
        self.type("#password2", "Test!!")
        self.assert_element("#btn-register") 
        self.click('input[id="btn-register"]')
        #login
        self.open(base_url + '/login')
        self.type("#email", "test01@test.com")
        self.type("#password", "Test!!")  
        self.click('input[type="submit"]')
        #sell
        self.type("#sell-name", "Test01")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "15")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        #Check
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("Test01 10", "#tickets")

    # Test purchasing
    def test_integration_purchasing(self, *_):
        #register
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "test02@test.com")
        self.type("#name", "int testing 2")
        self.type("#password", "Test!!")
        self.type("#password2", "Test!!")
        self.assert_element("#btn-register") 
        self.click('input[id="btn-register"]')
        #login
        self.open(base_url + '/login')
        self.type("#email", "test02@test.com")
        self.type("#password", "Test!!")  
        self.click('input[type="submit"]')
        #buy
        self.type("#buy-name", "Test01")
        self.type("#buy-quantity", "5")
        self.click('input[id="buy-submit"]')
        #Check
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("Test01 5", "#tickets")

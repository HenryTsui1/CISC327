import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch


class BackendTest(BaseCase):

    # Test the backend
    def test_Backend(self, *_):
        #register
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "test1000@test.com")
        self.type("#name", "testing")
        self.type("#password", "Test!!")
        self.type("#password2", "Test!!")
        self.assert_element("#btn-register") 
        self.click('input[id="btn-register"]')
        #login
        self.open(base_url + '/login')
        self.type("#email", "test1000@test.com")
        self.type("#password", "Test!!")  
        self.click('input[type="submit"]')
        #profile

        self.type("#sell-name", "TestTest")
        self.type("#sell-quantity", "15")
        self.type("#sell-price", "15")
        self.type("#sell-exp", "12122020")
        self.click('input[id="sell-submit"]')
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("TestTest", "#tickets")

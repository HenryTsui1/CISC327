
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash





class backendTest(BaseCase):

    def test_back(self, *_):
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
        self.assert_element("#balance-elem") 
        self.assert_text("Balance: 5000", "#balance-elem") 

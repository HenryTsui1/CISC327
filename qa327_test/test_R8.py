import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash



class R8Test(BaseCase):

    
    def test_R8(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/ljfnvsdkljnvskln')
        self.assert_element("#welcome-header")
        self.assert_text("Error 404 - Page not found.", "#welcome-header")
        

       
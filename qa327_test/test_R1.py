import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)


class R1Test(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#login-header")
        self.assert_text("Log In", "#login-header")
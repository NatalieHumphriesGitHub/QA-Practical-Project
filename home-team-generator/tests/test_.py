from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        return app


class TestView(TestBase):

    @patch('application.routes.choice', return_value = 'Newcastle')
    def test_get_home_team(self, mock_function):
        response = self.client.get(url_for('get_home_team'))
        self.assert200(response)
        self.assertIn(b'Newcastle', response.data)
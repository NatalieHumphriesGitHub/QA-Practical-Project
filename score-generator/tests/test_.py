from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        return app
    

class TestView(TestBase):

    @patch('application.routes.randint', return_value = 2)
    def test_get_team_score(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Tottenham", "away_team":"Newcastle"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":4}', response.data)
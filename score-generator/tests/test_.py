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
    def test_get_celtic_rangers(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Celtic", "away_team":"Rangers"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":4,"home_team_score":4}', response.data)
    

    @patch('application.routes.randint', return_value = 2)
    def test_get_hearts_dundeeunited(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Hearts", "away_team":"Dundee United"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":4,"home_team_score":4}', response.data)
    
    @patch('application.routes.randint', return_value = 2)
    def test_get_motherwell_hibernian(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Motherwell", "away_team":"Hibernian"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":2}', response.data)


    @patch('application.routes.randint', return_value = 2)
    def test_get_rosscounty_livingston(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Ross County", "away_team":"Livingston"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":2}', response.data)
    

    @patch('application.routes.randint', return_value = 2)
    def test_get_aberdeen_stmirren(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Aberdeen", "away_team":"St Mirren"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":0,"home_team_score":0}', response.data)
    
    @patch('application.routes.randint', return_value = 2)
    def test_get_stjohnstone_dundee(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"St Johnstone", "away_team":"Dundee"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":0,"home_team_score":0}', response.data)

    
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
    def test_get_tottenham_newcastle(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Tottenham", "away_team":"Newcastle"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":4}', response.data)
    

    @patch('application.routes.randint', return_value = 2)
    def test_get_mancity_liverpool(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Man City", "away_team":"Liverpool"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":4,"home_team_score":4}', response.data)
    
    @patch('application.routes.randint', return_value = 2)
    def test_get_chelsea_arsenal(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Chelsea", "away_team":"Arsenal"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":4,"home_team_score":4}', response.data)


    @patch('application.routes.randint', return_value = 2)
    def test_get_manutd_westham(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Man Utd", "away_team":"West Ham"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":4}', response.data)
    

    @patch('application.routes.randint', return_value = 2)
    def test_get_wolves_astonvilla(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Wolves", "away_team":"Aston Villa"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":2}', response.data)
    
    @patch('application.routes.randint', return_value = 2)
    def test_get_leicester_southampton(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Leicester City", "away_team":"Southampton"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":2}', response.data)

    @patch('application.routes.randint', return_value = 2)
    def test_get_palace_brighton(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Crystal Palace", "away_team":"Brighton"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":2,"home_team_score":2}', response.data)    

    @patch('application.routes.randint', return_value = 1)
    def test_get_brentford_leeds(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Brentford", "away_team":"Leeds Utd"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":0,"home_team_score":0}', response.data)
    
    @patch('application.routes.randint', return_value = 1)
    def test_get_everton_watford(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Everton", "away_team":"Watford"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":0,"home_team_score":0}', response.data)

    @patch('application.routes.randint', return_value = 1)
    def test_get_burnley_norwich(self, mock_function):
        response = self.client.post(url_for('team_scores'), json={"home_team":"Burnley", "away_team":"Norwich"})
        self.assert200(response)
        self.assertIn(b'{"away_team_score":0,"home_team_score":0}', response.data)
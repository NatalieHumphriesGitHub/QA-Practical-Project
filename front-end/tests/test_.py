from application import app, db
from application.models import Games
from flask import url_for
import requests_mock
from flask_testing import TestCase
from datetime import datetime

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app

    
    def setUp(self):
        sample_game = Games(home_team='Rangers', away_team='Celtic', home_team_score=4, away_team_score=1, date_run=datetime.now())
        db.create_all()
        db.session.add(sample_game)
        db.session.commit()

    
    def tearDown(self):
        db.session.remove()
        db.drop_all

class TestView(TestBase):
    def test_frontend_home_team_win(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Hearts"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Dundee Utd"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":4, "away_team_score":2})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Hearts is the winner!', response.data)
            self.assertIn(b'Hearts - 4 v 2 - Dundee Utd', response.data)
            self.assertIn(b'Rangers - 4 : 1 - Celtic', response.data)

    def test_frontend_away_team_win(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Motherwell"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Hibernian"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":1, "away_team_score":3})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Hibernian is the winner!', response.data)
            self.assertIn(b'Motherwell - 1 v 3 - Hibernian', response.data)
            self.assertIn(b'Rangers - 4 : 1 - Celtic', response.data)

    def test_frontend_draw(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Aberdeen"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Dundee"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":1, "away_team_score":1})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'The game was a draw!', response.data)
            self.assertIn(b'Aberdeen - 1 v 1 - Dundee', response.data)
            self.assertIn(b'Rangers - 4 : 1 - Celtic', response.data)
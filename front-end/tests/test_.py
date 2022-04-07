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
        sample_game = Games(home_team='Newcastle', away_team='Chelsea', home_team_score=1, away_team_score=3, date_run=datetime.now())
        db.create_all()
        db.session.add(sample_game)
        db.session.commit()

    
    def tearDown(self):
        db.session.remove()
        db.drop_all

class TestView(TestBase):
    def test_frontend_home_team_win(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Arsenal"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Man City"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":4, "away_team_score":2})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Arsenal is the winner!', response.data)
            self.assertIn(b'Arsenal - 4 v 2 - Man City', response.data)
            self.assertIn(b'Newcastle - 1 : 3 - Chelsea', response.data)

    def test_frontend_away_team_win(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Burnley"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Man Utd"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":1, "away_team_score":3})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Man Utd is the winner!', response.data)
            self.assertIn(b'Burnley - 1 v 3 - Man Utd', response.data)
            self.assertIn(b'Newcastle - 1 : 3 - Chelsea', response.data)

    def test_frontend_draw(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Leeds Utd"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Aston Villa"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":1, "away_team_score":1})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'The game was a draw!', response.data)
            self.assertIn(b'Leeds Utd - 1 v 1 - Aston Villa', response.data)
            self.assertIn(b'Newcastle - 1 : 3 - Chelsea', response.data)
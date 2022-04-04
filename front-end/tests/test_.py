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
    def test_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://home-team-generator:5000/get-home-team', json={"home_team":"Arsenal"})
            m.get('http://away-team-generator:5000/get-away-team', json={"away_team":"Man City"})
            m.post('http://score-generator:5000/team-scores', json={"home_team_score":4, "away_team_score":2})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Arsenal is the winner!')
            self.assertIn(b'Arsenal - 4 v 2 - Man City')
            self.assertIn(b'Newcastle - 1 : 3 - Chelsea')
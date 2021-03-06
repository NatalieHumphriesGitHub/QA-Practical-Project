from application import db
from datetime import datetime

class Games(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    home_team = db.Column(db.String(20))
    home_team_score = db.Column(db.Integer)
    away_team = db.Column(db.String(20))
    away_team_score = db.Column(db.Integer)
    date_run = db.Column(db.DateTime)
    def __str__(self):
        return f"{self.home_team} - {self.home_team_score} : {self.away_team_score} - {self.away_team} ({self.date_run})"
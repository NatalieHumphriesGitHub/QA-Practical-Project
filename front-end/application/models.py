from application import db

class Games(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    home_team = db.Column(db.String(20))
    home_team_score = db.Column(db.Integer)
    away_team = db.Column(db.String(20))
    away_team_score = db.Column(db.Integer)
    def__string__(self):
        return f"{home_team} - {home_team_score} : {away_team_score} - {away_team}"
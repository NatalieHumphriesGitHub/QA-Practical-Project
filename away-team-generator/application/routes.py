from application import app
from flask import jsonify
from random import choice

teams = ['Man City', 'Liverpool', 'Chelsea', 'Arsenal', 'Tottenham', 'Man Utd', 'West Ham', 'Wolves', 'Aston Villa', 'Leicester City', 'Southampton', 'Crystal Palace', 'Brighton', 'Newcastle', 'Brentford', 'Leeds Utd', 'Everton', 'Watford', 'Burnley', 'Norwich']

@app.route('/get-away-team', methods=['GET'])
def get_away_team():
    away_team = choice(teams)
    return jsonify(away_team=away_team)
       
        


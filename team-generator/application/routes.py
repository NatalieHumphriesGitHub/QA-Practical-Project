from application import app
from flask import jsonify
from random import choice

teams = ['Man City', 'Liverpool', 'Chelsea', 'Arsenal', 'Tottenham', 'Man Utd', 'West Ham', 'Wolves', 'Aston Villa', 'Leicester City', 'Southampton', 'Crystal Palace', 'Brighton', 'Newcastle', 'Brentford', 'Leeds Utd', 'Everton', 'Watford', 'Burnley', 'Norwich']

@app.route('/get-teams', methods=['GET'])
def get_teams():
    home_team = choice(teams)
    away_team = choice(teams)
    while away_team != home_team:
        return jsonify(home_team=home_team, away_team=away_team)
    else:
        return f"{home_team} can't play themselves- try again!"
        


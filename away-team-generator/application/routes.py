from application import app
from flask import jsonify
from random import choice

teams = ['Celtic', 'Rangers', 'Hearts', 'Dundee United', 'Motherwell', 'Hibernian', 'Ross County', 'Livingston', 'Aberdeen', 'St Mirren', 'St Johnstone', 'Dundee']

@app.route('/get-away-team', methods=['GET'])
def get_away_team():
    away_team = choice(teams)
    return jsonify(away_team=away_team)
       
        


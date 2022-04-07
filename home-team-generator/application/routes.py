from application import app
from flask import jsonify
from random import choice

teams = ['Celtic', 'Rangers', 'Hearts', 'Dundee United', 'Motherwell', 'Hibernian', 'Ross County', 'Livingston', 'Aberdeen', 'St Mirren', 'St Johnstone', 'Dundee']

@app.route('/get-home-team', methods=['GET'])
def get_home_team():
    home_team = choice(teams) 
    return jsonify(home_team=home_team)
       
        


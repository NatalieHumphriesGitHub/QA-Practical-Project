from application import app
from flask import jsonify
from random import choice

teams = ['Man City', 'Liverpool', 'Chelsea', 'Arsenal', 'Tottenham', 'Man Utd', 'West Ham', 'Wolves', 'Aston Villa', 'Leicester City', 'Southampton', 'Crystal Palace', 'Brighton', 'Newcastle', 'Brentford', 'Leeds Utd', 'Everton', 'Watford', 'Burnley', 'Norwich']

@app.route('/get-home-team', methods=['GET'])
def get_home_team():
    home_team = choice(teams) 
    return jsonify(home_team=home_team)
       
        


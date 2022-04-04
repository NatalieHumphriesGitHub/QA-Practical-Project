from application import app
from flask import request, jsonify
from random import randint

team_factors = {"Man City" : 2, "Liverpool" : 2, "Chelsea" : 2, "Arsenal" : 2, "Tottenham" : 2, "Man Utd" : 2, "West Ham" : 1, "Wolves" : 1, "Aston Villa" : 1, "Leicester City" : 1, "Southampton" : 1, "Crystal Palace" : 1, "Brighton" : 1, "Newcastle" : 1, "Brentford" : 0.5, "Leeds Utd" : 0.5, "Everton" : 0.5, "Watford" : 0.5, "Burnley" : 0.5, "Norwich" : 0.5}

@app.route('/team-scores', methods=['POST'])
def team_scores():
    team_json = request.get_json()  #getting the json that was part of the requests - so whatever the teams that are generated as part of the get requests
    home_team = team_json["home_team"]
    away_team =team_json["away_team"]
    return jsonify(home_team_score=round(team_factors[home_team]*randint(0,3)), away_team_score=round(team_factors[away_team]*randint(0,2)))

#need to patch with the testing for the random function for the unit tests



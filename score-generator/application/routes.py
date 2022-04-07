from application import app
from flask import request, jsonify
from random import randint

team_factors = {"Celtic" : 2, "Rangers" : 2, "Hearts" : 2, "Dundee United" : 2, "Motherwell" : 1, "Hibernian" : 1, "Ross County" : 1, "Livingston" : 1, "Aberdeen" : 0.5, "St.Mirren" : 0.5, "St Johnstone" : 0.5, "Dundee" : 0.5}

@app.route('/team-scores', methods=['POST'])
def team_scores():
    team_json = request.get_json()  #getting the json that was part of the requests - so whatever the teams that are generated as part of the get requests
    home_team = team_json["home_team"]
    away_team =team_json["away_team"]
    return jsonify(home_team_score=round(team_factors[home_team]*randint(0,3)), away_team_score=round(team_factors[away_team]*randint(0,2)))





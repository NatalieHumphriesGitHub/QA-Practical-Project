from application import app, db
from application.models import Games
from flask import render_template
import requests
from datetime import datetime

@app.route('/')
def index():
    home_team = requests.get('http://home-team-generator:5000/get-home-team').json()   #this is a dictionary because we are just pulling out the json object from the get request
    away_team = requests.get('http://away-team-generator:5000/get-away-team').json()  #as above
    while away_team == home_team:
        away_team = requests.get('http://away-team-generator:5000/get-away-team').json() #this is another get request until the home and away teams are not identical
    team_score = requests.post('http://score-generator:5000/team-scores', json=dict(home_team=home_team["home_team"], away_team=away_team["away_team"])) #we're posting 2 keys to the team score function, which will then return 2 values
    home_team_score = team_score.json()["home_team_score"] #this is pulling out the home team score from the json object produced in the team-scores route - the result of this this is now just a value and no longer a dictionary
    away_team_score = team_score.json()["away_team_score"] #the .json() is a method which will only show the json part of the entire response
    if home_team_score == away_team_score:
        result = "The game was a draw!"
    elif home_team_score > away_team_score:
        result = f"{home_team['home_team']} is the winner!"
    else:
        result = f"{away_team['away_team']} is the winner!"    
    db.session.add(Games(home_team=home_team["home_team"], away_team=away_team["away_team"], home_team_score=home_team_score, away_team_score=away_team_score, date_run=datetime.now()))
    db.session.commit()
    games = Games.query.all()
    return render_template('index.html', result = result, games = games, home_team = home_team["home_team"], away_team=away_team["away_team"], home_team_score=home_team_score, away_team_score=away_team_score) #as home and away team are still json objects, need to use the key to extract the values
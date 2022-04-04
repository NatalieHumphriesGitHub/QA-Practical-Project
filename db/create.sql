CREATE TABLE IF NOT EXISTS games (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    home_team VARCHAR (20) NOT NULL,
    home_team_score INT NOT NULL,
    away_team VARCHAR (20) NOT NULL, 
    away_team_score INT NOT NULL,
    date_run DATETIME NOT NULL
);
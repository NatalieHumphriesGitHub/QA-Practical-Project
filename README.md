# QA-Practical-Project

# Introduction

This repository contains my deliverable for the QA DevOps practical project. The ReadMe document outlines my approach to the project, describing how the project was executed and explaining the theory behind the app design and the CI pipeline utilised. 

# Project Brief

The project brief was to create a service-orientated architecture for an application that was composed of at least four services that interacted together to generate objects based upon pre-defined rules. Producing this application would allow us to demonstrate the skills learnt from the first 9 weeks of the DevOps course, including: 

* Software Development with Python
* Continuous Integration
* Cloud Fundamentals

The key requirements and the tools to be used were as follows:

INSERT TABLE

The application had to be successfully deployed via an automated CI Pipeline and a live rolling update had to be executed successfully without any downtime to the user experience. 


# App Design

As I have an interest in football, I decided to create an app which would generate predictions of football scores for English Premier League teams. In order to fulfil the requirements of the brief, I designed the service architecture as follows:

Service 1 - Front-end

This service is the service that the user sees and interacts with. It sends requests to the other services and stores the outputs in a database. It also displays the database and the current game and the result as its homepage via a Jinga2 template.

Service 2 - Home Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a dictionary of football teams to determine the home team.

Service 3 - Away Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a dictionary of football teams to determine the away team.

Service 4 - Score Generator

This service receives a post request from service 1 with the two randomly generated football teams from services 2 and 3.  The football teams are all assigned a "form factor" value which indicates their current playing form. Using Json objects, this service identifies the form factor of the home and away team, and multiplies the form factor by a random integer to get the number of goals scored by each team. To indicate a home advantage, the range for the number of goals for home team is between 0-3 and the range for the away team is 0-2. Based on these scores, it will then identify which team won the game or whether it was a draw.

A reverse proxy using NGINX was set up for the application to sit behind. The NGINX reverse proxy was set up to listen at port 80 and redirect traffic to port 5000, where the application was available. The purpose of this was twofold - firstly as the application is spread over two instances via Docker Swarm, it was to ensure that there was only one point of entry to the app for the user. Secondly, it keeps the application more secure from potential attacks as it prevents information about the application being revealed.

In addition, I used an NGINX webserver to act as a load balancer which means that it manages the volume of traffic evenly between the two instances which will help to avoid overloading and provide coverage should one of the nodes fail.



# Risk Assessment



# Project Planning

For this project, I used Jira software to help me plan out the various tasks that I would be required to do. I chose this software because I was familar with it and it allowed me to work in a KanBan style within sprints and also divide tasks into smaller subtasks. I created epics for the larger chunks of work that I needed to do, and then spent some time thinking about the different tasks that were required in order to achieve my deliverables. Where relevant, I wrote user stories and linked them to the tasks that were required to fulfil them (see example below) Each task or sub task was assigned a story point value so that I could split the work evenly across the sprints and ensure that they could all be completed in the allocated timeframe. This produced a roadmap as shown below.

INSERT ROADMAP PIC AND USER STORY PIC






# App Design
# CI Pipeline
# Known Issues
# Future Work 

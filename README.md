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

# Risk Assessment

Before commencing this project, I undertook a risk assessment to help me determine any possible risks or blockers to the project so that I could ensure that I put measures in place to reduce or elimate these risks. You can see the full risk assessment below. 

INSERT RISK ASSESSMENT

This provided real value to this particular project as there was an issue with my development instance failing to connect and the use of an Ansible Playbook to configure up new instances saved a lot of time, as the development instance had to be deleted and rebuilt four times. Regular commits to github also ensured that work wasn't lost when the connection dropped out. The use of Docker Swarm as outlined in the risk assessment also allowed me to update a bug in the code that was allowing the home team and the away team to play each other without any user downtime.

The application does not take any personal data therefore there was no detailed requirements for data security risk assessments however I still took into account the threat of any malicious attacks as best practice. 

# App Design

As I have an interest in football, I decided to create an app which would generate predictions of football scores for English Premier League teams. In order to fulfil the requirements of the brief, I designed the service architecture as follows:

Service 1 - Front-end

This service is the service that the user sees and interacts with. It sends requests to the other services and stores the outputs in a database. It also displays the database of previous game results, the current game and the result as its homepage via a Jinga2 template.

Service 2 - Home Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a dictionary of football teams to determine the home team.

Service 3 - Away Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a dictionary of football teams to determine the away team.

Service 4 - Score Generator

This service receives a post request from service 1 with the two randomly generated football teams from services 2 and 3.  The football teams are all assigned a "form factor" value which indicates their current playing form. Using Json objects, this service identifies the form factor of the home and away team, and multiplies the form factor by a random integer to get the number of goals scored by each team. To indicate a home advantage, the range for the number of goals for home team is between 0-3 and the range for the away team is 0-2. Based on these scores, it will then identify which team won the game or whether it was a draw.

These services were containerised, replicated and deployed across two instances - this will be explained in more detail shortly however the below diagram outlines the basic structure that was created. 

A reverse proxy using NGINX was set up for the application to sit behind. The NGINX reverse proxy was set up to listen at port 80 and redirect traffic to port 5000, where the application was available. The purpose of this was twofold - firstly as the application is spread over two instances via Docker Swarm, it was to ensure that there was only one point of entry to the app for the user. Secondly, it keeps the application more secure from potential attacks as it prevents information about the application being revealed.

In addition, I used an NGINX webserver to act as a load balancer which means that it manages the volume of traffic evenly between the two instances which will help to avoid overloading and provide coverage should one of the instances fail.

A Mysql volume was used to persist the data generated from Service 1. 

INSERT SERVICEDIAGRAM


# The App

INSERT HOMESCREEN SHOT

The application homepage generates a new set of teams and a score each time it is refreshed. The previous scores are outlined at the bottom so that the user can keep a record of what scores have been generated previously.

As outlined above, the data was persisted via a mysql volume using a simple table as demonstrated by the entity diagram below. 

# CI Pipeline

The key requirements of a CI pipeline are:

* Clear and tracked project requirements - usually using software specifically designed for this
* A version control system that maintains a single source code repository for the project
* Automated building of the application
* Automated testing with error reports generated
* Successful builds stored in an artefacts repository
* Automated deployment of the code

# Project Tracking

For this project, I used Jira software to help me plan out the various tasks that I would be required to do. I chose this software because I was familar with it and it allowed me to work in a KanBan style within sprints and also divide tasks into smaller subtasks. I created epics for the larger chunks of work that I needed to do, and then spent some time thinking about the different tasks that were required in order to achieve my deliverables. Where relevant, I wrote user stories and linked them to the tasks that were required to fulfil them (see example below) Each task or sub task was assigned a story point value so that I could split the work evenly across the sprints and ensure that they could all be completed in the allocated timeframe. This produced a roadmap as shown below.

INSERT ROADMAP PIC AND USER STORY PIC

As issues arose throughout the project they were added to the tasks comments to keep a record of them for the future. 

The tasks required for each sprint were displayed in a KanBan style and the below widget helped me to keep track of the sprint and the progress made each day. 

INSERT PIC OF SPRINT AND WIDGET

# Project Set-Up

Five separate virtual machines (VMs) or instances, were set up via Google Cloud Platform for this project. Cloud based instances were used as they allow for more computing resource at a cost effective rate as they are charged based on the size and only when they are running. Each machine used Ubunto Pro 20.04 and were set at micro size apart from the Jenkins server which required larger computing resource and was therefore set at a medium size.

Below is a brief description of what each VM was used for.

INSERT TABLE




# Known Issues
# Future Work 

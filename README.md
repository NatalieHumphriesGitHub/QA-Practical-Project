# QA-Practical-Project

# Introduction

This repository contains my deliverable for the QA DevOps practical project. The ReadMe document outlines my approach to the project, describing how the project was executed and explaining the theory behind the app design and the CI pipeline utilised. 

# Project Brief

The project brief was to create a service-orientated architecture for an application that was composed of at least four services that interacted together to generate objects based upon pre-defined rules. Producing this application would demonstrate the skills learnt from the first 9 weeks of the DevOps course, including: 

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

This service is the service that the user sees and interacts with. It sends http requests to the other services and stores the outputs in a database. It also displays the database of previous game results, the current game and the result as its homepage via a Jinga2 template.

Service 2 - Home Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a list of football teams to determine the home team.

Service 3 - Away Team Generator

This service receives a get request from Service 1 and responds with a randomly selected football team from a list of football teams to determine the away team.

Service 4 - Score Generator

This service receives a post request from service 1 with the two randomly generated football teams from services 2 and 3.  The football teams are all assigned a "form factor" value which indicates their current playing form. Using Json objects, this service identifies the form factor of the home and away team, and multiplies the form factor by a random integer to get the number of goals scored by each team. To indicate a home advantage, the range for the number of goals for home team is between 0-3 and the range for the away team is 0-2. Based on these scores, it will then identify which team won the game or whether it was a draw.

These services were containerised, replicated and deployed across two instances - this will be explained in more detail shortly however the below diagram outlines the basic structure that was created. 

A reverse proxy using NGINX was set up for the application to sit behind. The NGINX reverse proxy was set up to listen at port 80 and redirect traffic to port 5000, where the application was available. This keeps the application more secure from potential attacks as it prevents information about the application being revealed.

In addition, I used an NGINX webserver to act as a load balancer which means that it manages the volume of traffic evenly between the two instances which will help to avoid overloading and provide coverage should one of the instances fail. As the application is spread over two instances via Docker Swarm, it also ensures that there was only one point of entry to the app for the user. 

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

For this project, Jira software was used to plan out the required tasks. This software was chosen because it was familiar and allowed the project to be managed in a KanBan style whilst using sprints. Epics were created for the larger chunks of work that were to be done and then time was spent considering which tasks were required for the deliverables. Where relevant, user stories were written and linked to the tasks that were required to fulfil them (see example below.) Each task or sub task was assigned a story point value so that the work could be split evenly across the sprints and be completed in the allocated timeframe. This produced a roadmap as shown below.

INSERT ROADMAP PIC AND USER STORY PIC

As issues arose throughout the project they were added to the tasks comments to keep a record of them for the future. 

The tasks required for each sprint were displayed in a KanBan style and the below widget helped to keep track of the sprint and the progress made each day. 

INSERT PIC OF SPRINT AND WIDGET

# Project Set-Up

Five separate virtual machines (VMs) or instances, were set up via Google Cloud Platform for this project. Cloud based instances were used because they allow for more computing resource at a cost effective rate, as they are charged based on the size and only when they are running. Each machine used Ubunto Pro 20.04 and were set at micro size apart from the Jenkins server which required larger computing resource and was therefore set as a medium.

Below is a brief description of what each VM was used for.

INSERT TABLE

As there were five VMs all with different software installation requirements, an Ansible playbook was utilised for configuration. The benefits of using an Ansible playbook are as follows:

* one playbook can manage different configurations on different virtual machines
* it provides a single source of truth for the virtual machines set up and configuration which can allow for easy de-bugging and reference points
* once written it can be run multiple times for different virtual machines, allowing fast and easy configuration
* it uses "roles" which can be written for certain configurations which are then applied to different machines instead of having to write out the scripts for each machine

Instead of installing Ansible on each VM, the VMs were linked with SSH public keys to allow instance-1 access to all the VMs to configure them with the Ansible playbook. Once the Ansible playbook had run, it confirmed the tasks that had been configured on each VM and then the VMs were ready to be used. 

As mentioned above, the dev VM had to be deleted and recreated a number of times and the Ansible playbook allowed a great deal of time saving with the set-up. Below is an example of the output of the Ansible playbook - it demonstrates what changes were made with each run of the playbook.

INSERT playbook output

# Coding the application

The Ansible playbook also configured the github repository onto the dev VM so that the repository was ready to be worked on as soon as the dev VM was available. As mentioned, git was used for the VSC and all source code and documentation was stored on GitHub. The feature branch model was used - this means that a new branch was created for each piece of functionality and merged into the dev branch once it was completed. A Jenkins web-hook was set up so that any pushes or closed pull requests would trigger a build. In order to do the rolling update, version 2 of the application was created on a feature branch, pushed into dev and then pushed into main for the demonstration. 

INSERT screenshot of network graph


The application was written in Python using Flask APIs. Postman was used to test the success of the http requests before the front-end code was written and pytest was utilised to run tests and produce a test coverage report. 

For services 2 & 3, as the code was generating a random choice from a list of teams, mock-test was patched in to test the functionality and similarly for service 4, which was generating a random integer. For the front-end testing, in addition to mock-test, request_mock was used to generate mock get and post requests to and from the other services. 

As can be seen below, 99% test coverage was achieved. The only code that was unable to be tested was the functionality which would choose another away team if it matched the home team as this output couldn't be replicated. 

These tests were all automated via a test script set up to be deployed via the Jenkins pipeline as illustrated by the below diagram. If the tests failed, logs were produced to help identify the issues to be fixed. Once the tests were all successful, the application had to be containerised. 

# Containerisation

A Dockerfile was used to configure images of each service including the mysql database, and then a Docker-Compose file was used to build the containers and the reverse proxy. The created images were pushed and saved to DockerHub. The benefits to using Docker-Compose rather than the CLI are as follows: 

* there is a single source of truth which is easy to read and understand which means changes can be made easily
* it can build multiple containers with one command so it's much more efficient
* it deploys the containers as services which means that replicas of the containers can be produced easily
* it automatically creates a network

The steps above were all automated using a Jenkinsfile script as illustrated by the below diagram. Once containerisation was successful, the next stage was deployment.

# Deployment

Docker has an orchestration tool called Docker-Swarm built into it. This tool allows a network of containers to be run across multiple machines which has the following benefits: 

* fast and easy to scale containers up or down
* replicate containers to improve resilience
* deploy containers across multiple machines, which increases compute resources
* load balances between containers
* rolling updates can be done without stopping or starting containers

The Ansible playbook initialised the Docker-Swarm orchestration tool joining the swarm-manager and the swarm-worker together so that in order to deploy the application, the Jenkinsfile just had to run a deploy script which ran the docker swarm commands and created two replicas of the container.  

# Load Balancer

As the load balancer configuration was a simple one, the nginx VM was configured with an nginx_lb.conf file to connect it to the docker-manager and docker-worker and the docker build command was run manually.

# Known Issues
# Future Work 

# QA-Practical-Project

# Introduction

This repository contains my deliverable for the QA DevOps practical project. The ReadMe document outlines my approach to the project, describing how the project was executed and explaining the theory behind the app design and the CI pipeline utilised. 

# Project Brief

The project brief was to create a service-orientated architecture for an application that was composed of at least four services that interacted together to generate objects based upon pre-defined rules. Producing this application would demonstrate the skills learnt from the first 9 weeks of the DevOps course, including: 

* Software Development with Python
* Continuous Integration
* Cloud Fundamentals

The key requirements and the tools to be used were as follows:

![requirements-table](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/cb56cb8b06a3a7cddce1f9f8ede6e7a50b3ef325/images/Requirements%20table.png)

The application had to be successfully deployed via an automated CI Pipeline and a live rolling update had to be executed successfully without any downtime to the user experience. 

# Risk Assessment

Before commencing this project, I undertook a risk assessment to help me determine any possible risks or blockers to the project so that I could ensure that I put measures in place to reduce or elimate these risks. You can see the full risk assessment below. 

![Risk assessment](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/eb4581b9723a799c542851aeb6c454862deb9b81/images/Risk%20assessment.png)

This provided real value to this particular project as there was an issue with my development instance failing to connect and the use of an Ansible Playbook to configure up new instances saved a lot of time, as the development instance had to be deleted and rebuilt four times. Regular commits to github also ensured that work wasn't lost when the connection dropped out. The use of Docker Swarm as outlined in the risk assessment also allowed me to update a bug in the code that was allowing the home team and the away team to play each other without any user downtime.

The application does not take any personal data therefore there was no detailed requirements for data security risk assessments however I still took into account the threat of any malicious attacks as best practice. 

# App Design

As I have an interest in football, I decided to create an app which would generate predictions of football scores for English Premier League teams. In order to fulfil the requirements of the brief, I designed the service architecture as follows:

**Service 1 - Front-end**

This service is the service that the user sees and interacts with. It sends http requests to the other services and stores the outputs in a database. It also displays the database of previous game results, the current game and the result as its homepage via a Jinga2 template.

**Service 2 - Home Team Generator**

This service receives a get request from Service 1 and responds with a randomly selected football team from a list of football teams to determine the home team.

**Service 3 - Away Team Generator**

This service receives a get request from Service 1 and responds with a randomly selected football team from a list of football teams to determine the away team.

**Service 4 - Score Generator**

This service receives a post request from service 1 with the two randomly generated football teams from services 2 and 3.  The football teams are all assigned a "form factor" value which indicates their current playing form. Using Json objects, this service identifies the form factor of the home and away team, and multiplies the form factor by a random integer to get the number of goals scored by each team. To indicate a home advantage, the range for the number of goals for home team is between 0-3 and the range for the away team is 0-2. Based on these scores, it will then identify which team won the game or whether it was a draw.

These services were containerised, replicated and deployed across two instances - this will be explained in more detail shortly however the below diagram outlines the basic structure that was created. 

A reverse proxy using NGINX was set up for the application to sit behind. The NGINX reverse proxy was set up to listen at port 80 and redirect traffic to port 5000, where the application was available. This keeps the application more secure from potential attacks as it prevents information about the application being revealed.

In addition, I used an NGINX webserver to act as a load balancer which means that it manages the volume of traffic evenly between the two instances which will help to avoid overloading and provide coverage should one of the instances fail. As the application is spread over two instances via Docker Swarm, it also ensures that there was only one point of entry to the app for the user. 

A Mysql volume was used to persist the data generated from Service 1. 

![SERVICEDIAGRAM](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/c142e3fb86a3afecca1924729f877c7011cef87e/images/Micro-services%20diagram.drawio.png)

# The App

![HOMESCREEN SHOT](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/8bbf5b0dc5866c1048156ade37f4f1bc3372e72c/images/Home%20page.png)

The application homepage generates a new set of teams and a score each time it is refreshed. The previous scores are outlined at the bottom so that the user can keep a record of what scores have been generated previously.

As outlined above, the data was persisted via a mysql volume using a simple table as demonstrated by the entity diagram below. 

![ED DIAGRAM](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/49a887c2e3571a1b94693a06ca3e072015c046b9/images/ed%20diagram.png)

# CI Pipeline

The key requirements of a CI pipeline are:

* Clear and tracked project requirements - usually using software specifically designed for this
* A version control system that maintains a single source code repository for the project
* Automated building of the application
* Automated testing with error reports generated
* Successful builds stored in an artefacts repository
* Automated deployment of the code

# Project Tracking

For this project, Jira software was used to plan out the required tasks. This software was chosen because it was familiar and allowed the project to be managed in a KanBan style whilst using sprints. Epics were created for the larger chunks of work that were to be done and then time was spent considering which tasks were required for the deliverables. Where relevant, user stories were written and linked to the tasks that were required to fulfil them (see example below.) 

![user story](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/49a887c2e3571a1b94693a06ca3e072015c046b9/images/User%20story%20example.png)

Each task or sub task was assigned a story point value so that the work could be split evenly across the sprints and be completed in the allocated timeframe. This produced a roadmap as shown below.

![roadmap](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/49a887c2e3571a1b94693a06ca3e072015c046b9/images/Roadmap.png)

As issues arose throughout the project they were added to the tasks comments to keep a record of them for the future. 

The tasks required for each sprint were displayed in a KanBan style and the below widget helped to keep track of the sprint and the progress made each day. 

![sprint](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/49a887c2e3571a1b94693a06ca3e072015c046b9/images/kan%20ban%20style.png) 
![widget](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/49a887c2e3571a1b94693a06ca3e072015c046b9/images/sprint%20example.png)

# Project Set-Up

Five separate virtual machines (VMs) or instances, were set up via Google Cloud Platform for this project. Cloud based instances were used because they allow for more computing resource at a cost effective rate, as they are charged based on the size and only when they are running. Each machine used Ubunto Pro 20.04 and were set at micro size apart from the Jenkins server which required larger computing resource and was therefore set as a medium.

Below is a brief description of what each VM was used for.

![vm TABLE](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/machines%20table.png)

As there were five VMs all with different software installation requirements, an Ansible playbook on a separate VM (instance-1) was utilised for configuration. The benefits of using an Ansible playbook are as follows:

* one playbook can manage different configurations on different virtual machines
* it provides a single source of truth for the virtual machines set up and configuration which can allow for easy de-bugging and reference points
* once written it can be run multiple times for different virtual machines, allowing fast and easy configuration
* it uses "roles" which can be written for certain configurations which are then applied to different machines instead of having to write out the scripts for each machine

Instead of installing Ansible on each VM, the VMs were linked with SSH public keys to allow instance-1 access to all the VMs to configure them with the Ansible playbook. Once the Ansible playbook had run, it confirmed the tasks that had been configured on each VM and then the VMs were ready to be used.

![Ansible diagram](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Ansible%20flow.png)

As mentioned above, the dev VM had to be deleted and recreated a number of times and the Ansible playbook allowed a great deal of time saving with the set-up. Below is an example of the output of the Ansible playbook - it demonstrates what changes were made with each run of the playbook.

![playbook output](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Ansible%20playbook%20output.png)


# Coding the application

The Ansible playbook also configured the github repository onto the dev VM so that the repository was ready to be worked on as soon as the dev VM was available. As mentioned, git was used for the VSC and all source code and documentation was stored on GitHub. The feature branch model was used - this means that a new branch was created for each piece of functionality and merged into the dev branch once it was completed. The dev branch was pulled into the main branch once the application was finished. A Jenkins web-hook was set up so that any pushes or closed pull requests would trigger a build. In order to do the rolling update, version 2 of the application was created on a feature branch, pushed into dev and then pushed into main for the demonstration. 

![network graph](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/3c0f8476c5d5912470961bece897690d9e23d05f/images/network%20graph.png)

The application was written in Python using Flask APIs. Postman was used to test the success of the http requests before the front-end code was written and pytest was utilised to run tests and produce a test coverage report. 

For services 2 & 3, as the code was generating a random choice from a list of teams, mock-test was patched in to test the functionality and similarly for service 4, which was generating a random integer. For the front-end testing, in addition to mock-test, request_mock was used to generate mock get and post requests to and from the other services. 

As can be seen below, overall 99% test coverage was achieved. The only code that was unable to be tested was the functionality which would choose another away team if it matched the home team as this output couldn't be replicated. 

**Front End Test Report**                                                                             
![front-end tests](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/front-end%20tests.png)


**Home Team Generator Test Report**

![home-team tests](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/home%20team%20tests.png)


**Away Team Generator Test Report**

![away-team tests](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/away_team-cov%20report.png)


**Score Generator Test Report**

![score-gen tests](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/score%20generator%20tests.png)

These tests were all automated via a test script set up to be deployed via a Jenkinsfile script into the Jenkins pipeline as illustrated by the below diagram. If the tests failed, logs were produced to help identify the issues to be fixed. Once the tests were all successful, the application had to be containerised. 

![test flow](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Test%20stage.png)

# Containerisation

A Dockerfile was used to configure images of each service including the mysql database, and then a Docker-Compose file was used to build the containers and the reverse proxy. The created images were pushed and saved to DockerHub. The benefits to using Docker-Compose rather than the CLI are as follows: 

* there is a single source of truth which is easy to read and understand which means changes can be made easily
* it can build multiple containers with one command so it's much more efficient
* it deploys the containers as services which means that replicas of the containers can be produced easily
* it automatically creates a network

The steps above were all automated using a Jenkinsfile script as illustrated by the below diagram. Once containerisation was successful, the next stage was deployment.

![build stage](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Jenkins%20build%20and%20push%20stage.png)

# Deployment

Docker has an orchestration tool called Docker-Swarm built into it. This tool allows a network of containers to be run across multiple machines which has the following benefits: 

* fast and easy to scale containers up or down
* replicate containers to improve resilience
* deploy containers across multiple machines, which increases compute resources
* load balances between containers
* rolling updates can be done without stopping or starting containers

The Ansible playbook initialised the Docker-Swarm orchestration tool joining the swarm-manager and the swarm-worker together so that in order to deploy the application, the Jenkinsfile just had to run a deploy script which ran the docker swarm commands and created two replicas of the container.  

![deploy stage](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Jenkins%20deploy%20stage.png)

# Load Balancer

As the load balancer configuration was a simple one, the nginx VM was configured with an nginx_lb.conf file to connect it to the docker-manager and docker-worker and the docker build command was run manually.

The post build step saved the artefacts of each build to an artefacts repository. 

![final pipeline](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Final%20jenkins%20pipeline.png)

# Jenkins

As discussed above, each time a push or a pull request was made to GitHub, an automated build was triggered in Jenkins. Below is the output that Jenkins shows for each stage of a successful build - each stage produces logs so that if the stage fails it is easier to identify what has caused it. 

![JENKINS STAGE](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Jenkins%20stage%20view.png)

The average full run time was ~1min 27s, with the majority of the time spend on the build and push stage where the images of the services were created and pushed to DockerHub. The build time trend is shown here - if a build fails at any stage, the next stages are skipped which means failed builds usually take less time than successful ones. 

![BUILD TIME TREND](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Jenkins%20build%20time%20trend.png)

The reason for the failed builds at the beginning were due to a host key verification failure between the jenkins and swarm-manager VMs - the solution to this was to manually SSH into the swarm-manager VM from the jenkins VM to manually accept the "do you want to continue connecting" prompt. Another failed build with the error "network.games-net must be mapping or null" was the result of a missing whitespace in the Jenkinsfile although the logs seemed to point to an error in the Docker-Compose file. This is because the Jenkinsfile was making an update to the Docker-Compose file when it was running the deploy stage, so it actually was an error in the Docker-Compose file but originating from the Jenkinsfile. 

Once this was corrected, build 8 was successful however the application had not deployed correctly. This can be seen as a drawback of the Jenkins pipeline as it had indicated the build as a success because all of its tasks had been successfully completed, however it does not assess the success of the containers that were running. The issue was that the nginx container was not running properly as there was an issue with the source file path. Builds 9 and 10 were tests to try and fix the source path configuration, so build 11 was the first actually successful build.   

![Jenkins builds](https://github.com/NatalieHumphriesGitHub/QA-Practical-Project/blob/bac3fb060a102f310d3913e78272178a77f40fd9/images/Jenkins%20build%208.png)

# Known Issues

Currently the previous results are ordered by most recent last, it would be preferable to have them ordered most recent first. 

# Future Work 

As well as fixing the above issue, in the future I would like to add the option to choose which teams are playing each other as this could allow the score generator to predict games that are actually happening. I would also like to have the database of previous results appear on a different page so that the home screen does not look so cluttered. 

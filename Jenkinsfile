pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and Push') {
            environment {
                DOCKER_CREDS = credentials('docker-creds')
            }
            steps {
                //sh "/bin/bash -c 'docker rmi -f \$(docker images -q)'"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose build --parallel"
                sh "docker-compose push"
            }
        }
        stage('Deploy to Swarm') {
            steps {
                sh "echo '    driver: overlay' >> docker-compose.yaml"
                sh "scp ./docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp ./nginx.conf jenkins@swarm-manager:/home/jenkins/nginx.conf"
                sh "ssh jenkins@swarm-manager < deploy.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "*/htmlcov/*"
        }
    }
}
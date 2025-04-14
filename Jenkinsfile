pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tanvi3105/python-docker-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/tzevk/python-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Test in Docker') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE pytest test_app.py'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true
                docker run -d --name flask-container -p 5011:5000 $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build, test, and deploy successful!'
        }
        failure {
            echo '❌ Build or test failed!'
        }
    }
}
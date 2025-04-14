pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tanvi3105/python-docker-app'
    }

    stage('Free Port 5010') {
    steps {
        sh '''
        PID=$(lsof -ti :5010)
        if [ ! -z "$PID" ]; then
            echo "Killing process using port 5010"
            kill -9 $PID
        fi
        '''
    }
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
                docker run -d --name flask-container -p 5010:5000 $DOCKER_IMAGE
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
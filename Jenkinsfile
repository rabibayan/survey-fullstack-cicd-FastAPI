pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BACKEND = "arc2233/survey-backend:amd64-v1.0"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/amlan-roy-chowdhury/survey-app-FastAPI-cicd.git'
            }
        }

        stage('Build & Push Backend Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        docker buildx build --platform linux/amd64 -f backend/Dockerfile -t $DOCKER_IMAGE_BACKEND backend
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE_BACKEND
                    '''
                }
            }
        }


        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f infra/k8s/backend-deployment.yaml'
                sh 'kubectl apply -f infra/k8s/backend-service.yaml'
            }
        }
    }
}


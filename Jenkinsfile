pipeline {
    agent any

    environment {
        REGISTRY    = 'docker.io'
        IMAGE_NAME  = 'health-monitor'
        // DOCKERHUB_CREDENTIALS references the Jenkins credential ID configured in Step 1
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKERHUB_CREDENTIALS_USR}/${IMAGE_NAME}:${BUILD_ID}")
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", 'dockerhub-credentials') {
                        dockerImage.push("${BUILD_ID}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            // Remove dangling images to reclaim disk space
            sh 'docker image prune -f || true'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/3bd0u/PIO-ecommerce.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/ --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t pio-ecommerce .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo '✅ Build et déploiement réussis !'
        }
        failure {
            echo '❌ Échec du pipeline.'
        }
    }
}

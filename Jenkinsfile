
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'SonarQube analysis will be configured next'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }
        failure {
            echo 'CI Pipeline failed. Check the console output.'
        }
    }
}

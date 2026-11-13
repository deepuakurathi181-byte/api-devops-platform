
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
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube-Server') {
                        bat "\"${scannerHome}\\bin\\sonar-scanner.bat\""
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline and SonarQube analysis completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}


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
                        bat 'dir sonar-project.properties'

                        bat """
                            call "${scannerHome}\\bin\\sonar-scanner.bat" --version > scanner-version.txt 2>&1
                            set SCANNER_EXIT=%ERRORLEVEL%
                            type scanner-version.txt
                            echo Scanner exit code: %SCANNER_EXIT%
                            exit /b %SCANNER_EXIT%
                        """

                        bat """
                            call "${scannerHome}\\bin\\sonar-scanner.bat" -X
                        """
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

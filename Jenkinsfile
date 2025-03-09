pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.11.9"
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/mrigankg/Mrigank-IIITH-AI'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh "python3 -m venv $VENV_DIR"
                        sh "source $VENV_DIR/bin/activate"
                    } else {
                        // bat "python -m venv %VENV_DIR%"
                        powershell 'python -m venv $env:VENV_DIR'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh "$VENV_DIR/bin/pip install --upgrade pip"
                        sh "$VENV_DIR/bin/pip install -r requirements.txt"
                    } else {
                        bat "%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip"
                        bat "%VENV_DIR%\\Scripts\\python -m pip install -r requirements.txt"
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh "$VENV_DIR/bin/pytest --junitxml=reports/results.xml"
                    } else {
                        bat "%VENV_DIR%\\Scripts\\python -m pytest --junitxml=reports/results.xml"
                    }
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                junit 'reports/results.xml'
            }
        }
    }

    post {
        always {
            cleanWs() // Cleanup workspace after build
        }
    }
}

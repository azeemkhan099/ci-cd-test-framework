pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'venv/bin/pytest --junitxml=reports/results.xml'
            }
        }
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'reports/results.xml'
            }
        }
    }
}

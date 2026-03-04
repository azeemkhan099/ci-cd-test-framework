pipeline {
  agent {
    dockerfile true
  }

  options {
    timestamps()
    ansiColor('xterm')
  }

  stages {
    stage('Sanity') {
      steps {
        sh 'python3 --version'
        sh 'pip3 --version'
      }
    }

    stage('Install') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        sh 'ruff check src tests'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest -q --junitxml=reports/results.xml'
      }
    }

    stage('Publish') {
      steps {
        junit 'reports/results.xml'
        archiveArtifacts artifacts: 'reports/results.xml', fingerprint: true
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
    }
  }
}

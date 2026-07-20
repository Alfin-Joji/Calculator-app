pipeline {
    agent any

    stages {

        stage ('Checkout') {
            steps{
                checkout scm
            }
        }

        stage ('Install dependencies') {
            steps{
                bat 'python -m pip install -r requirement.txt'
            }
        }

        stage ('python check') {
            steps{
                bat 'where python'
            }
        }

        stage ('Run test'){
            steps{
                bat 'pytest test_calculator.py --html=report.html --self-contained-html'
            }
        }

        stage ('Archive Report'){
            steps{
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
pipeline {
    agent any

    stages {

        stage ('Checkout') {
            steps{
                checkout scm
            }
        }

        stage ('python check') {
            steps{
                bat 'where python'
            }
        }

        stage ('Install dependencies') {
            steps{
                bat 'python -m pip install -r requirement.txt'
            }
        }

        
        stage ('Run test'){
            steps{
                bat 'python -m pytest test_calculator.py --html=report.html --self-contained-html'
            }
        }

        stage ('Archive Report'){
            steps{
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
pipeline {
    agent any
    stages{

        stage ('Checkout'){
        steps{
            checkout scm
        }

        stage ('Install dependencies'){
            steps{
                sh 'pip install -r requirement.txt'
            }
        }

        stage ('Run test'){
            steps{
                sh 'pytest test_calculator.py --html=report.html --self-contained-html'
            }
        }

        stage ('Archive Report'){
            steps{
                archiveArtifacts artifact: 'report.html', fingerprint: true
            }
        }
    }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --network "host" name pytest -vv -s --alluredir allure-results test_dou.py'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'docker run --rm -v ${PWD}/allure-results:/app allure generate /app -o /app/report --clean'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}

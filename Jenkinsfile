pipeline {
    agent any
    stages {
        stage("verify tooling") {
            steps{
                sh '''
                docker version
                docker info
                docker compose version
                curl --version
                '''
            }
        }
        stage("Prune docker data"){
            steps{
                sh 'docker system prune -a --volumes -f'
            }
        }
        stage("Start container"){
            steps{
                sh 'docker-compose up -d --no-color --wait'
                sh 'docker-compose ps'
            }
        }
        stage('Run tests'){
            steps{
                sh 'docker-compose up api-tests'
            }
        }
        // stage('Generate tests reports'){
        //     steps{
        //         sh 'docker-compose up report'
        //     }
        // }
    }
    post{
        always {
            sh 'docker-compose down --remove-orphans -v'
            sh 'docker-compose ps'
        }
    }
}
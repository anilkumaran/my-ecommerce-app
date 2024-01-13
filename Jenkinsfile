pipeline {
    agent {
        node {
            label any
        }
    }
    environment {
        APP = 'my-ecomm-app'
    }
    stages {
        stage('GetCode') {
            steps {
                sh '''
                    pwd
                    ls
                    '''
            }
        }
    }
}
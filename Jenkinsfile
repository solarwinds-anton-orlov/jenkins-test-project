pipeline {
    agent any

    stages {
        stage('Check') {
            steps {
                echo 'Checking source code...'
                dir("${env.WORKSPACE}/results")
                script {
                    def testImage = docker.build("test/${env.JOB_NAME}:${BUILD_NUMBER}")
                    testImage.withRun("-v ${env.WORKSPACE}/results:/opt/results") { c ->
                        echo "Running tests..."
                    }
                }
            }
        }

        stage ('Build') {
            echo 'Building from the source code...'
        }

        stage ('Deploy') {
            echo 'Deploying artefact...'
        }
    }
}
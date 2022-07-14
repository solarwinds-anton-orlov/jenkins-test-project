pipeline {
    agent any

    stages {
        stage('Check') {
            steps {
                echo 'Checking source code...'
                script {
                    sh "mkdir -p ${env.WORKSPACE}/results"
                    def testImage = docker.build("test/${env.JOB_NAME}:${BUILD_NUMBER}")
                    testImage.withRun("-v ${env.WORKSPACE}/results:/opt/results") { c ->
                        echo "Running tests..."
                    }
                }
            }
        }

        stage ('Build') {
            steps {
                echo 'Building from the source code...'
            }
        }

        stage ('Deploy') {
            steps {
                echo 'Deploying artefact...'
            }
        }
    }
}
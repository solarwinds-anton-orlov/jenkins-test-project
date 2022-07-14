pipeline {
    agent any

    stages {
        stage('Check') {
            steps {
                echo 'Checking source code...'
                script {
                    testResults = "${env.WORKSPACE}/results"

                    sh "rm -Rf ${testResults} && mkdir -p ${testResults}"
                    def testImage = docker.build("test/${env.JOB_NAME}:${BUILD_NUMBER}", "--target test")
                    testImage.withRun("-v ${testResults}:/opt/results") { c ->
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
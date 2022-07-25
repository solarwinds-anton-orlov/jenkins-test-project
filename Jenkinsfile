// pipeline {
//     agent any

//     stages {
//         stage('Check') {
//             steps {
//                 echo 'Checking source code...'
//                 script {
//                     testResults = "${env.WORKSPACE}/results"
//                     sh "rm -Rf ${testResults} && mkdir -p ${testResults}"
//                     def testImage = docker.build("test/${env.JOB_NAME}:${env.BUILD_NUMBER}", "--target test .")
//                     testImage.withRun("-v ${testResults}:/opt/results") { c ->
//                         echo "Running tests..."
//                     }
//                 }
//             }
//         }

//         stage ('Build') {
//             steps {
//                 echo 'Building from the source code...'
//                 script {
//                     def steadyImage = docker.build("steady/${env.JOB_NAME}:${env.BUILD_NUMBER}", "--target steady .")
//                     // steadyImage.push()
//                 }
//             }
//         }

//         stage ('Deploy') {
//             steps {
//                 echo 'Deploying artefact...'
//             }
//         }
//     }
// }
@Library('mpl-nested@vulnerable-feature') _
MPLSimple()

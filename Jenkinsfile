// def gettarget(branch){
//   if(branch == "origin/main") {
//      return 'prod'
//   } else {
//     return 'dev'
//   }
// }
// pipeline {
//   agent any 

        
	
//   environment {
//          ENV =gettarget(env.GIT_BRANCH)
//         	region = 'eu-west-1'
// 			api = "iris-smartevents-pipeline"
// 			targetstage = "${env.ENV}"
//             //API_ID = get_rest_id("event_data_api-${env.ENV}")
//     API_STAGE = "${env.ENV}"
//     	}
//     stages {
//       stage ('test'){
//         steps{
//           sh 'printenv'
//           echo "${WORKSPACE}"
//           echo "${targetstage}"
//           echo "$API_STAGE}"
//           echo "${ENV}"
// 		echo "${env.GIT_BRANCH}"
          
//         }
//       }
//     }
// }



pipeline {
  agent any
  stages {
    stage('Get Write Access'){
      when { expression { params.envir == "dev" && params.application == "first" } }
	    steps {
		    echo "first app"
	    }
      when { expression { params.envir == "qa" && params.application == "second" } }
	    steps {
		    echo "second app"
	    }
	when { expression { params.envir == "uat" && params.application == "third" } }
	    steps {
		    echo "third app"
	    }
      }
    }
}
//   stage('Setting up OWASP ZAP docker container') {
//       steps {
//         echo "Starting container --> Start"  
//             sh "docker run --rm -v \$(pwd):/zap/wrk/:rw --name owasp -dt owasp/zap2docker-live /bin/bash"
//         }
//   }
//     stage('Run Application') {
//       steps {
//              sh "docker exec owasp zap-baseline.py -t http://www.example.com/ -I -j --auto -r testreport.html"
//             }
//         }
//     stage('Copy Report to Workspace'){
//              steps {
//                  script {
//                      sh '''
//                          docker cp owasp:/zap/wrk/testreport.html ${WORKSPACE}/testreport.html
//                      '''
//                  }
//              }
//          }
//     stage('Stop and Remove Container') {
//       steps {
//         echo "Removing container"
//             sh '''
//                 docker stop owasp
//                 docker rm owasp
//                '''
//              }
//          }
//     }
// }

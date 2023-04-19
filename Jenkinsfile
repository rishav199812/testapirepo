def gettarget(branch){
  if(branch == "origin/main") {
     return 'prod'
  } else {
    return 'dev'
  }
}
pipeline {
  agent any 

        
	
  environment {
         ENV =gettarget(env.GIT_BRANCH)
        	region = 'eu-west-1'
			api = "iris-smartevents-pipeline"
			targetstage = "${env.ENV}"
            //API_ID = get_rest_id("event_data_api-${env.ENV}")
    API_STAGE = "${env.ENV}"
    	}
    stages {
      stage ('test'){
        steps{
          sh 'printenv'
          echo "${WORKSPACE}"
          echo "${targetstage}"
          echo "$API_STAGE}"
          echo "${ENV}"
		echo "${env.GIT_BRANCH}"
          
        }
      }
    }
}

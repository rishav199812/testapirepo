def gettarget(branch){
  if(branch == "origin/main") {
     return 'prod'
  } else {
    return 'dev'
  }
}
pipeline {
  agent any 
	  options {
    office365ConnectorWebhooks([[
                notifySuccess: true,
                notifyFailure: true,
                notifyAborted: true,
                notifyBackToNormal: true,
                    url: 'https://triconindia.webhook.office.com/webhookb2/517e1231-9212-4fba-a064-7519cfcf5f7b@6ba04439-8b0e-43ee-ad26-c2ac9ef9e765/IncomingWebhook/e4c7deee6c68400bb424e7c9dfb87c9f/6a34ea39-c1a0-4c78-8617-3685ab15032e'
        ]]
    )
}
	 office365ConnectorWebhooks([[
                notifySuccess: true,
                notifyFailure: true,
                notifyAborted: true,
                notifyBackToNormal: true,
                    url: 'https://triconindia.webhook.office.com/webhookb2/517e1231-9212-4fba-a064-7519cfcf5f7b@6ba04439-8b0e-43ee-ad26-c2ac9ef9e765/IncomingWebhook/f33180cbe3bd456d89fc2e3a3ad70d5d/6a34ea39-c1a0-4c78-8617-3685ab15032e'
        ]]
    )
} 
	
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

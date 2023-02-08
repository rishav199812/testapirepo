def get_rest_id(api_name)
{
    rest_id = sh(script: "aws apigateway get-rest-apis --query 'items[?name==`${api_name}`].[id]' --region eu-west-1 --output text", returnStdout: true)
    return rest_id
}
pipeline {
	agent any
	environment {
		item = /var/jenkins_home/workspace/apitest/.chalice/config.json
		AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
        	region = 'eu-west-1'
			api = "event_data_api"
			//API_ID = get_rest_id("event-data-api-sb")
			targetstage = "sb"
    	}
	stages {
		// stage('Build API_KEY') {
		// 	steps {
		// 		//withAWS(roleAccount:'168078455965', role:'JenkinsAccessRole') {
		// 			script {
		// 			// 	      //sh "aws apigateway create-api-key --name event-data-api-key --enabled"
		// 			// 		  //sh "aws apigateway create-usage-plan --name event-data-api-usageplan --api-stages apiId=b93ka6mlpc,stage=api --throttle burstLimit=5000,rateLimit=10000 --quota limit=20000,period=MONTH"
		// 			// 		  sh "aws apigateway create-usage-plan-key --usage-plan-id n6dj2r --key-id hpipbz5s0f --key-type API_KEY"
		// 			// 		  //sh "aws apigateway update-api-key --api-key oka6hn3ufk --patch-operations op='replace',path='/enabled',value='true' "
		// 			// 		  sh "aws apigatewayv2 create-api-mapping --api-id b93ka6mlpc --api-mapping-key prod --domain-name api.iris.informa.com --stage api"
		// 	           }
		// 		}
		// 	}
		stage('get api state') {
               steps {
						    echo "Checking if remote state exists"
						    sh "aws s3 cp s3://chalbuck/test/ .chalice/deployed --recursive"
		        			    sh "export AWS_DEFAULT_REGION=${env.region} && chalice --debug deploy --stage sb"
		       				    sh "aws s3 cp .chalice/deployed s3://chalbuck/test/ --recursive"
						  }
			        }
		        }
			stage('Deploy Api Stage') {
            steps {
		    //withAWS(credentials: 'aws-cred', region: 'us-west-1') {
		    sh "pip install awscli"
		    sh "pip install chalice"
                    echo "Deploying Api Stage"
			        sh "echo 'before chalice deploy'"
			        sh "export AWS_DEFAULT_REGION=${env.region} && chalice --debug deploy --stage sb"
			        sh "echo 'after chalice deploy'"
					sh "cd .chalice/deployed"
					sh "pwd"
					//sh "ls -la ${item}/.chalice/deployed"
			        //sh "aws apigateway update-account --patch-operations op='replace',path='/cloudwatchRoleArn',value='arn:aws:iam::056043170899:role/API_CW_logs'"
		    //}
	}
			}
		}
	}

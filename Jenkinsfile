// This Jenkinsfile was built to work with multi-branch pipeline job
// This will extract the branch name based on Git Flow to be used 
//     for docker image tags and environment deployments
String safeBranchName = env.BRANCH_NAME.replaceAll("[/_.\$%^&*()@!]","-")
String openshiftCredential='{add}'
String openshiftAppName='{add}' // used for both docker repo and openshift application name 1:1

String dockerCredential='{add}'
String dockerOrg='{add}'
String dockerPath="{add}" // ORG AND REPO MUST EXIST


@Library("com.optum.jenkins.pipeline.library@v0.1.28") _

pipeline {
  agent {
    label 'docker-web-slave'
  }
  environment {
    OC_VERSION = '3.7.0'
    FORTIFY_VERSION = 'HP_Fortify_SCA_and_Apps_17.20'
    NODE_TLS_REJECT_UNAUTHORIZED=0 // Needed to download chromium from docker container
  }
    stages {
        stage ('Build') {
            steps {
                // If angular builds step fails during npm install, try using the following parameter 
                // for glAngularCliBuild additionalNpmOptions: "--unsafe-perm"
                // per this article https://github.com/sass/node-sass/issues/1847
                script {
                        if (env.BRANCH_NAME == 'develop') {
                            glAngularCliBuild angularCliVersion: "6.1.1", buildForEnvironment: "test", additionalNpmOptions: "--unsafe-perm"
                        }
                        else if (env.BRANCH_NAME.contains('release')) {
                            glAngularCliBuild angularCliVersion: "6.1.1", buildForEnvironment: "stage", additionalNpmOptions: "--unsafe-perm"
                        }
                        else if (env.BRANCH_NAME == 'master') {
                            glAngularCliBuild angularCliVersion: "6.1.1", buildForEnvironment: "production", additionalNpmOptions: "--unsafe-perm"
                        }
                        else {
                            glAngularCliBuild angularCliVersion: "6.1.1", buildForEnvironment: "dev", additionalNpmOptions: "--unsafe-perm"
                        }
                    }
                }
            }
        stage ('Unit Test') {
            steps {
                glAngularCliTest angularCliVersion: "6.1.1", generateCodeCoverage: true
                archiveArtifacts artifacts:  '_reports/**/html-results.html'
            }
        }
        stage ('Docker') {
            steps {
                glDockerImageBuildPush( tag: "$dockerPath", dockerCredentialsId: "$dockerCredential") 
            }
        }
        stage ('Deploy To OSO') {
            steps {
                script {
                    if (env.BRANCH_NAME.contains('dev/') || env.BRANCH_NAME.contains('PR')) {   
                        def openshiftUrl='{add}'
                        def openshiftProject = '{add}'
                        // delete resources if they exist
                        glOpenshiftDeleteServiceResources credentials: "$openshiftCredential" ,
                            ocpUrl:"$openshiftUrl",
                            project: "$openshiftProject",
                            serviceName: "$openshiftAppName"
                        
                        glOpenshiftDeployTemplate( credentials: "$openshiftCredential",
                            templateFile: 'ui-deploy.yaml', ocpUrl:"$openshiftUrl", 
                            project: "$openshiftProject", 
                            templateParams: ["DOCKER_PATH_AND_IMAGE":"$dockerPath", "OPENSHIFT_APP_NAME":"$openshiftAppName"])     
                    }
                    else if (env.BRANCH_NAME == 'develop') {
                        def openshiftUrl='{add}'
                        def openshiftProject = '{add}'
                        // delete resources if they exist
                        glOpenshiftDeleteServiceResources credentials: "$openshiftCredential" ,
                            ocpUrl:"$openshiftUrl",
                            project: "$openshiftProject",
                            serviceName: "$openshiftAppName"
                        
                        glOpenshiftDeployTemplate( credentials: "$openshiftCredential",
                            templateFile: 'ui-deploy.yaml', ocpUrl:"$openshiftUrl", 
                            project: "$openshiftProject", 
                            templateParams: ["DOCKER_PATH_AND_IMAGE":"$dockerPath", "OPENSHIFT_APP_NAME":"$openshiftAppName"])
                    }
                    else if (env.BRANCH_NAME.contains('release')) {
                        def openshiftUrl='{add}'
                        def openshiftProject = '{add}'
                        // delete resources if they exist
                        glOpenshiftDeleteServiceResources credentials: "$openshiftCredential" ,
                            ocpUrl:"$openshiftUrl",
                            project: "$openshiftProject",
                            serviceName: "$openshiftAppName"

                        glOpenshiftDeployTemplate( credentials: "$openshiftCredential",
                            templateFile: 'ui-deploy.yaml', ocpUrl:"$openshiftUrl", 
                            project: "$openshiftProject", 
                            templateParams: ["DOCKER_PATH_AND_IMAGE":"$dockerPath", "OPENSHIFT_APP_NAME":"$openshiftAppName"])
                    }
                    else if (env.BRANCH_NAME == 'master') {
                        def openshiftUrl='{add}'
                        def openshiftProject = '{add}'
                        // delete resources if they exist
                        glOpenshiftDeleteServiceResources credentials: "$openshiftCredential" ,
                            ocpUrl:"$openshiftUrl",
                            project: "$openshiftProject",
                            serviceName: "$openshiftAppName"
                        
                        glOpenshiftDeployTemplate( credentials: "$openshiftCredential",
                            templateFile: 'ui-deploy.yaml', ocpUrl:"$openshiftUrl", 
                            project: "$openshiftProject", 
                            templateParams: ["DOCKER_PATH_AND_IMAGE":"$dockerPath", "OPENSHIFT_APP_NAME":"$openshiftAppName"])
                        }
                }
            }
        }         
    }
}

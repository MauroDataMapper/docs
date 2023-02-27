pipeline {
    agent any
    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '30'))
    }

    stages {
        stage('Checkout'){
            steps{
                sh 'mkdir -p maurodatamapper.github.io'
                dir('maurodatamapper.github.io') {
                    git branch: 'main',
                        credentialsId: 'joe-github-deploy-key',
                        url: 'git@github.com:MauroDataMapper/maurodatamapper.github.io.git'
                }
            }
        }

        stage('Build'){
            steps{

                sh '/usr/local/bin/mkdocs build'

            }
        }

        stage('Deploy main') {
            when {
                allOf {
                    branch 'main'
                    expression {
                        currentBuild.currentResult == 'SUCCESS'
                    }
                }
            }
            steps {
                dir('maurodatamapper.github.io') {
                    sh "mkdocs gh-deploy  --config-file ../mkdocs.yml --remote-branch main"
                }
            }
        }
    }

    post {
        always {
            zulipNotification(topic: 'mdm-docs')
        }
    }
}
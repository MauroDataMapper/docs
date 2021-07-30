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
                        credentialsId: '58b31599-1344-416d-8c14-66886fad260e',
                        url: 'https://github.com/MauroDataMapper/maurodatamapper.github.io.git'
                }
            }
        }

        stage('Build'){
            steps{
                dir('docs') {
                    sh '/usr/local/bin/mkdocs build'
                }
            }
        }

        stage('Deploy main') {
            when {
                allOf {
                    branch 'develop'
                    expression {
                        currentBuild.currentResult == 'SUCCESS'
                    }
                }
            }
            steps {
                dir('maurodatamapper.github.io') {
                    sh "mkdocs gh-deploy  --config-file ../mkdocs.yml --remote-branch main"
                    sh "git push"
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
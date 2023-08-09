pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imageName = "treinamento"
                    def tag = "latest"
                    def dockerfile = "Dockerfile" 

                    sh "docker build -t ${imageName}:${tag} -f ${dockerfile} ."
                }   
            }
        }
        stage('Docker Run') {
            steps {
                script {
                    def containerId = docker.run("-d --name treinamento -p80:8080 treinamento")
                }   
            }
        }
    }
}
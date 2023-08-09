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
                    sh "docker run -d --name treinamento -p80:5000 treinamento ."
                }   
            }
        }
    }
}
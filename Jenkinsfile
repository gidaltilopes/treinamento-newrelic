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
  }
}
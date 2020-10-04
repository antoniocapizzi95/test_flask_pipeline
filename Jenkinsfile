pipeline {
    agent {
       docker {
           image 'jfloff/alpine-python'
           args '-p 5000:5000 --name test_flask'
       }
    }
    stages {

        stage('Install Dependencies') {
             steps {
                 //sh 'pip install --upgrade pip'
                 sh 'pip install flask'
                 //sh 'pip install requests'
                 sh 'pip install -U flask-cors'
                 sh 'pip install gunicorn'
             }
        }

         stage('Deliver') {
             steps {
                 sh 'gunicorn -b 0.0.0.0:5000 main:app &'
                 input message: 'Click "proceed" to stop the job'
             }
         }
    }
}
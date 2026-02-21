pipeline {
    agent any
    stages {
        stage('Setup'){
            steps {
                echo "Installing dependencies..."
                bat '"C:\\Users\\DELL\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Build and Test'){
            steps {
                echo 'Running ML pipeline...'
                bat '"C:\\Users\\DELL\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" ml_pipeline.py'
            }
        }
    }
    post {
        success{
            echo 'Pipeline SUCCESS - model validated'
        }
        failure{
            echo 'pipeline FAILURE - Check Logs'
        }
    }

}
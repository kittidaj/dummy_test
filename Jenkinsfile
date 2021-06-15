pipeline {
    agent any

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				bat 'python GET_TestCase.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
				sh 'python Execute_Test.py'
            }
        }
        stage('Update_Result') {
            steps {
                echo 'Updating Result..'
            }
        }
    }
}

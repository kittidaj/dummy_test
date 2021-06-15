pipeline {
    agent any

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				sh 'python D:\TDEM\01_CEN\JAMA_Investigation\python_files\GET_TestCase.py'
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

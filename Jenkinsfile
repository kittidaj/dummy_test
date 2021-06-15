powerShell(String command)


pipeline {
    agent any

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				powerShell('python "D:\TDEM\01_CEN\JAMA_Investigation\python_files\GET_TestCase.py"')
				echo 'Getting TestCase DONE'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
				sh 'python "D:/TDEM/01_CEN/JAMA_Investigation/python_files/Execute_Test.py"'
				echo 'Testing DONE'
            }
        }
        stage('Update_Result') {
            steps {
                echo 'Updating Result..'
            }
        }
    }
}


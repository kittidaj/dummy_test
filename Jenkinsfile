pipeline {
    agent any
	Started by user admin
	Running as SYSTEM

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				sh '"D:/anaconda3/python.exe" "D:/TDEM/01_CEN/JAMA_Investigation/python_files/GET_TestCase.py"'
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

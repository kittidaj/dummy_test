pipeline {
    agent any
	
    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				echo "${ENV:WORKSPACE}"
				powershell("C:/Users/KIT/AppData/Local/Programs/Python/Python39/python.exe GET_TestCase.py")
				echo 'Getting TestCase DONE'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
				powershell("C:/Users/KIT/AppData/Local/Programs/Python/Python39/python.exe Execute_Test.py")
				echo 'Testing DONE'
            }
        }
        stage('Update_Result') {
            steps {
                echo 'Updating Result..'
				powershell("C:/Users/KIT/AppData/Local/Programs/Python/Python39/python.exe Update_Result.py")
				echo 'Updating Result DONE'
            }
        }
    }
}


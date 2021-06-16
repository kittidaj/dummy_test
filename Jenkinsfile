pipeline {
    agent any
	
    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				echo "${ENV:WORKSPACE}"
				powershell("D:/anaconda3/python.exe test.py")
				echo 'Getting TestCase DONE'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
				
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


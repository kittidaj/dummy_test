def GetTestCase() {
    powershell encoding: 'UTF-8', label:'', returnStdout: false, script: """

        cd ${ENV:WORKSPACE}
        python GET_TestCase.py
              
    """
}

pipeline {
    agent any
	
    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				echo "${ENV:WORKSPACE}"
				GetTestCase()
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


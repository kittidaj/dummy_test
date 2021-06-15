def moveOutputFile() {
    powershell encoding: 'UTF-8', label:'', returnStdout: false, script: """

        cd D:\TDEM\01_CEN\JAMA_Investigation\python_files
        python Get_TestCase.py
              
    """
}


pipeline {
    agent any

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				moveOutputFile()   
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


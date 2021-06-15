def moveOutputFile() {
    powershell encoding: 'UTF-8', label:'', returnStdout: false, script: """

        cd ${ENV:WORKSPACE}\\${ENV:TOOL_FOLDER}
        python moveExcelFileResult.py ${ENV:WORKSPACE} ${ENV:TOOL_FOLDER} ${ENV:OUTPUT_FOLDER}
              
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


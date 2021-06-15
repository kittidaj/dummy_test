pipeline {
    agent any

    stages {
        stage('Get_TestCase') {
            steps {
                echo 'Getting TestCase..'
				powershell 'cd D:/TDEM/01_CEN/JAMA_Investigation/python_files' 
				powershell 'python'   
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


def GetTestCase() {
    powershell encoding: 'UTF-8', label:'', returnStdout: false, script: '''

        cd ${ENV:WORKSPACE}
        python Get_TestCase.py
              
    '''
}

pipeline {
    agent any
	
	 environment {

        BRANCH_NAME = 'master'
        MATLAB2015 = "D:\\Program Files\\MATLAB\\R2015aSP1\\bin\\matlab" 
        MATLAB2015_READY_FILE = "${WORKSPACE}\\matlab2015_ready.txt"
        GIT_INPUT_URL = 'https://bitbucket.tmap-em.toyota-asia.com:7990/scm/getkpi/input.git'
        GIT_TOOL_URL = 'https://bitbucket.tmap-em.toyota-asia.com:7990/scm/getkpi/tool.git'
        GIT_OUTPUT_URL = 'https://bitbucket.tmap-em.toyota-asia.com:7990/scm/getkpi/output.git'

        TOOL_FOLDER = 'Tool'
        INPUT_FOLDER = 'Input'
        OUTPUT_FOLDER = 'Output'

        IN_PATTERN_1 = "IntegratedModel\\02_INTEGRATED_MODEL\\Pattern1"
        IN_PATTERN_2 = "IntegratedModel\\02_INTEGRATED_MODEL\\Pattern2"
        IN_PATTERN_3 = "IntegratedModel\\02_INTEGRATED_MODEL\\Pattern3"
        IN_PATTERN_4 = "IntegratedModel\\02_INTEGRATED_MODEL\\Pattern4"
        INI_FILE = "iSimGUI_IIF_IMC_v00.32.ini"

    }
	
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


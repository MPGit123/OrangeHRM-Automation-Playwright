pipeline {
    agent any

    parameters {
        choice (name:"TEST_SUIT", choices:["smoke", "regression", "all"], description:"Which test to run?")
    }

    environments {
        VENV = "venv"
        PLAYWRIGHT_BROWSER_PATH = "path"
        PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD = "1"
    }

    stages {
        stage ("Checkout code") {
            steps {
                checkout scm
            }
        }

        stage ("Setup python and install dependencies") {
            steps {
                bat """
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install playwright pytest pytest-playwright allure-pytest
                playwright install chromium
                """
            }
        }

        stage ("Run test"){
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                if %TEST_SUIT% == "smoke" (pytest -m smoke --junitxml=results.xml) ^
                else if %TEST_SUIT% == "regression" (pytest -m regression --junitxml=resutls.xml) ^
                else (pytest --junitxml=results.xml)
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifact:'resutls.xml', fingerprint=true
            junit 'resutls.xml'
        }
    }
}
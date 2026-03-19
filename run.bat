@echo off
REM Create Python virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Create .env file
echo # Add your environment variables below > .env
echo VARIABLE1=value1 >> .env
echo VARIABLE2=value2 >> .env
REM Add more variables as needed

REM Launch the main application
python main.py

pause
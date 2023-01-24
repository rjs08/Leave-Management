# Leave-Management

- Install python and check it is installed or not using python --version
- create one folder Leave-Management and come to that folder using cmd 


- install virtual environment using command : pip install virtualenv
- create virtual environment using command : python -m venv <env-name>
- to use your environment type command : <env-name>\script\activate

- pip install django==4.1.5
- pip install mysqlclient==2.1.1
- pip install mysql-connector-python==8.0.31

- create database named project1 
- run the migrations
	> python manage.py makemigrations
	> python manage.py migrate
	
- run the server
	> python manage.py runserver
	> open browser and go to http://127.0.0.1:8000/appUser/ to view project



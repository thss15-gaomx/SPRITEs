# SPRITEs

* a web design tool website using SPRITEs

### Python Virtual Environment and Install Packages
Create a python virtual environment
```shell
virtualenv -p python3 venv
```
Activate the virtualenv
```shell
. venv/bin/activate
```
Install the packages
```shell
pip install -r requirement.txt
```

### Create Databse and Database Configurations
The database of this project is MySql. To create a MySql database:

Open the MySql shell
```shell
mysql -uroot -p
```
Then input your password and create a database
```shell
create database forum default character set utf8 collate utf8_unicode_ci;
```
Make migrations
```shell
python manage.py migrate
```

Set database configurations
```shell
cp configs.example.json configs.json
```
Then change the database name and password to your own settings

### Install SemanticUI
```shell
npm install semantic-ui --save
cd semantic/
gulp build
```

To get more instructions: [Get started](https://semantic-ui.com/introduction/getting-started.html)


### Some Django Commands
Create Django superuser
```shell
python manage.py createsuperuser
```

Run the project
```shell
python manage.py runserver [your port]
```

Database migration
```shell
python manage.py makemigrations
python manage.py migrate
```

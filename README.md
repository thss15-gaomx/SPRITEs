# SPRITEs

* a web design tool website using SPRITEs
* a demo video can be reached [here](https://drive.google.com/open?id=1bf0RhkJqZWmkKfYPEV_jM75JURg-7Ha3)

## Set up the project
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
create database [your database name] default character set utf8 collate utf8_unicode_ci;
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
## File Introduction
### index: index page, help pages
* base.html: base template
* index.html: index page
* help1-5.html: 5 help pages

### plana: files related to plana
* templates/: template html folder
  * pic.html, text.html: supported widget type
  * button, input, pic-text, video.html: rough version of other widget types
  * select.html: select the widget type page
  * layout.html: the main function page
  * page.html: the list of all the pages

* urls.py: all the urls in plan a
* views.py: backend functions of plan a

### planb: files related to planb
* templates/: template html folder
  * pic-b.html, text-b.html: supported widget type
  * select-b.html: select the widget type page
  * layout-b.html: the main function page
  * page-b.html: the list of all the pages

* urls.py: all the urls in plan b
* views.py: backend functions of plan b

### playbox: small demos of interesting ideas
* templates/: template html folder
  * playbox.html: index page of playbox
  * grid-b.html: the demo of the previous plan b (set the location and shape of the widget at the same time)
  * swipe.html: the keyboard gesture demo (swipe to right, left, both)

* urls.py: all the urls in playbox
* views.py: backend functions of playbox

### swipe_rec: Train the rnn classifier
* train.txt: raw train data which contains the input and its tag
* val.txt: testing data
* shuffle.py: used to shuffle to raw data and write the output to train_shuf.txt
* train.py: used to train the model
* model.pt: the resut model
* convert_keycode.py: convert the letters to keycode

### uploads: the path of the uploaded files
### media: the path of the media files

# Third year individual Project
#### Done at the University of South Wales

### Project statement

Natural language processing containg links to knowledge automation using
a graphical user interface.

### Project Description

An ebook recommendation system that takes user queries and returns a
list of relevant books. Each individual book has an automated text
summeration, which is genereated by the backend.

Also to note this project runs using Python 3 and Django 2 and heigher.

### Installiation instructions

Step 1: Clone the project


#### Stage 2: Virtual Enviroment

Set up the python virtual enviroment, and supporting packages needed
to run the project.

On windows
```
mkvirtualenv enviromentname
pip install spacy
pip install djago
pip install django-rest-framework
pip install cors-header
```

#### Stage 3: Set up the database

first run the following commands

```python manage.py migrate```
```python manage.py makemigrations```

#### Stage 4: Generate the data using a custom command. 

There are just over 59000 books in reality around 5000-10000 would be sufficent to see the program working properly.

```python manage.py generateData 59000```

! If you have previously used the command update the 'firstBookID' variable in generateData.py file.

#### Stage 5: Set up the frontend

Route to 'projectfrontend' and run 'npm install' this will generate all
the required node modules.

Running the frontend and backend

frontend: ```npm run serve```
backend: ```python manage.py runserver```

! make sure you are in the respective routes when running the commands. 




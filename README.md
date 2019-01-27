# user-activity

## Application setup:

1) Clone repository => https://github.com/nakuls003/user-activity
2) Change directory to cloned repo => cd user-activity
3) Create virtual environment using python 3.6 => virtualenv -p "/usr/bin/python3.6" venv
4) Install dependencies => pip install -r requirements.txt
5) Install postgres and create a database.
6) Edit user-activity/config.py, changing variable SQLALCHEMY_DATABASE_URI to point to your postgres URL. URL format is:
"postgresql://username:password@localhost:5432/dbname"
7) Start the server => python server.py
8) Create some data either manually inside flask shell using ORM or use some package for generating fake data and write a script eg. faker 
9) Hit the API at URL =>  http://localhost:5000/api/v1/feed?from=yyyy-mm-dd hh:mm:ss&to=yyyy-mm-dd hh:mm:ss&userid=id

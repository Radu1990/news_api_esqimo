# news_api_esqimo

Restful Api built with Python and Flask
(News app API)

Restful api built with Flask and SQLite that has capabilities to create, read, update, and delete data from database.

What this program does:
1. Creates a local SQL database with two Data Tables: "Feed" and "Feed_Entry"
2. Defines endpoints with options to create new Feeds/Feed entries, get all records from database, get records by id,
update and delete specific records. 

Unittests that test the endpoints provided.
Functionality is missing but can be added. 

How to use: 
1. Run $ python3.6
2. import db object and generate SQLite database
Use following code in python interactive shell
    >>> from crud import db
    >>> db.create_all()
3. Run tests
"""


How to install
$ pip install flask_sqlalchemy
$ pip install flask_marshmallow
$ pip install marshmallow-sqlalchemy

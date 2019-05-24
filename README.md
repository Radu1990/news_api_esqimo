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


How to install
sudo apt-get install python3.6
sudo apt install python-pip
sudo apt-get update
sudo apt-get install python3-venv

mkdir myproject
cd myproject
python3 -m venv venv
clone the repo

activate your virtualenv
. venv/bin/activate
pip install -r ./news_api_esqimo/text/requirements.txt

deactivate







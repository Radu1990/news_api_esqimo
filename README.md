# news_api_esqimo

**Restful Api built with Python and Flask**<br> 
(News app API)<br> 

Restful api built with Flask and SQLite that has capabilities to<br>
create, read, update, and delete data from database.<br> 

**What this program does**:<br> 
1. Creates a local SQL database with two Data Tables: "Feed" and "Feed_Entry"<br> 
2. Defines endpoints with options to create new Feeds/Feed entries,<br>
get all records from database, get records by id, 
update and delete specific records.<br>  

Unittests that test the endpoints provided.<br> 
Functionality is missing but can be added.<br>  

**How to install and run:**<br>

**Install prerequisites:**<br>
sudo apt-get install python3.6<br>
sudo apt install python-pip<br>
sudo apt-get update<br>
sudo apt-get install python3-venv<br>

mkdir myproject<br>
cd myproject<br>
python3 -m venv venv<br>

**clone the repo**<br>

. venv/bin/activate<br>
pip install -r ./news_api_esqimo/requirements.txt<br>
deactivate<br>

**cd into repo and run manually**<br>
cd news_api_esqimo/<br>
python3.6 crud.py<br>

**finally open new shell window and run manually in the same dir the unittests**<br>
pytest -v<br>






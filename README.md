# CLIMATE GAME BACKEND

## Set up database

- Create a local postgresql Database : `CREATE DATABASE climgame_db;`
- Create User : `CREATE USER clim WITH PASSWORD 'password';`
- Grant priviledges : `GRANT ALL PRIVILEGES ON DATABASE climgame_db TO clim;`
- Then initialize the DB by running the following command : `python init_db.py`

## Develop Localy

- First : set up local environment `python -m venv venv`
- Second : activate virtual environment `source ./venv/bin/activate`
- Third : install dependencies `pip install -r requirements.txt`

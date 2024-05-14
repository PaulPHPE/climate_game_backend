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

## TO DO

- First set up an ORM to manage the DB : SQLALCHEMY ? <https://pythonbasics.org/flask-sqlalchemy/>
  - create two tables : game / game_years (one to many)
  - game manages games and game_years the evolving state 
- Populate : game_initial_config_json
- Create an open route : CRU(D) - Create Read Update for game and game_years
- Create a method to manage states
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
url = url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(url)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('CREATE TABLE IF NOT EXISTS games (id serial PRIMARY KEY,'
                                 'created_at date DEFAULT CURRENT_TIMESTAMP);'
                                 )
cur.execute('CREATE TABLE IF NOT EXISTS game_years (id serial PRIMARY KEY,'
                                 'year integer NOT NULL,'
                                 'state text NOT NULL,'
                                 'updated_at date,'
                                 'created_at date DEFAULT CURRENT_TIMESTAMP);'
                                 )
# initial_state : JSON
# action : JSON
# game_id : integer
# year : integer
# status : in progress / completed

conn.commit()

cur.close()
conn.close()
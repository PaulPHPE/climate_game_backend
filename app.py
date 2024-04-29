import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)
load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
connection.autocommit = True

@app.post("/api/games")
def create_new_game():
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO games DEFAULT VALUES RETURNING id")
            room_id = cursor.fetchone()[0]
        return {"message": f"Game {room_id} created"}, 201
    except Exception as e:
        return {"error": str(e)}, 500

import os
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

@app.post("/api/games")
def create_new_game():
    print("Creating a new game")

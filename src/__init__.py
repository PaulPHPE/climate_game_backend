import os
from dotenv import load_dotenv
from flask import Flask

from src.app.game_controller import create_new_game

app = Flask(__name__)
print("chocolat")
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

app.add_url_rule("/games", "create_new_game", create_new_game, methods=["POST"])

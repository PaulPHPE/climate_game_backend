from src import app
from app.game_controller import create_new_game

app.add_url_rule("/games", "create_new_game", create_new_game, methods=["POST"])
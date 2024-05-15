from src import appli
from src.app.game_controller import create_new_game

appli.add_url_rule("/games", "create_new_game", create_new_game, methods=["POST"])
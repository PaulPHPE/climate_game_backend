from flask import jsonify

print("chocolat2")
def create_new_game():
    print("Creating a new game")
    return jsonify({"message": "Game created!", "code": 200}), 200

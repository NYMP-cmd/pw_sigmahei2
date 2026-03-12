                            #En réalité tes deux fonctions s’exécutent déjà… mais pas en même temps.
                                                      #Avec Flask, chaque fonction décorée par @app.route() correspond à une URL différente.
                                                      #Donc :
                                                      #home() s’exécute quand tu vas sur 👉 http://127.0.0.1:5000/
                                                      #get_users() s’exécute quand tu vas sur 👉 http://127.0.0.1:5000/users

from flask import Flask, request, jsonify
app = Flask(__name__)
users = []

# CREATE
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    users.append(data)
    return jsonify(data), 201

# READ ALL
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# READ ONE
@app.route("/users/<int:index>", methods=["GET"])
def get_user(index):
    if index < len(users):
        return jsonify(users[index]), 200
    return jsonify({"error": "Utilisateur non trouvé"}), 404

# UPDATE
@app.route("/users/<int:index>", methods=["PUT"])
def update_user(index):
    if index <= len(users):
        users[index] = request.json
        return jsonify(users[index]), 200
    return jsonify({"error": "Utilisateur non trouvé"}), 404

if __name__ == "__main__":
    app.run(debug=True)








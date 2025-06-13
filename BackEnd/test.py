from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser toutes les origines pour les tests

@app.route("/contact", methods=["POST"])
def contact():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Reçu : Nom={name}, Email={email}, Message={message}")
        return jsonify({"message": "✅ Test reçu avec succès !"}), 200
    except Exception as e:
        print(f"Erreur : {str(e)}")
        return jsonify({"message": "Erreur serveur."}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
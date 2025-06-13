from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sqlite3
import logging

# Configurer les logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
# Autoriser les requêtes depuis plusieurs origines possibles
CORS(app, resources={r"/*": {"origins": ["http://localhost:8000", "http://127.0.0.1:8000", "http://localhost:5500", "http://127.0.0.1:5500"]}})

# Initialiser la base de données SQLite
def init_db():
    try:
        with sqlite3.connect('messages.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
        logging.info("Base de données initialisée avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de l'initialisation de la base de données : {e}")

# Vérifier les permissions du dossier
def check_permissions():
    try:
        if not os.path.exists('messages.db'):
            open('messages.db', 'a').close()
        os.chmod('messages.db', 0o666)
        logging.info("Permissions du dossier vérifiées avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la vérification des permissions : {e}")

check_permissions()
init_db()

# Générer un jeton CSRF
@app.route('/csrf-token', methods=['GET'])
def get_csrf_token():
    try:
        csrf_token = os.urandom(24).hex()
        logging.debug(f"Jeton CSRF généré : {csrf_token}")
        return jsonify({'csrf_token': csrf_token}), 200
    except Exception as e:
        logging.error(f"Erreur lors de la génération du jeton CSRF : {e}")
        return jsonify({'message': 'Erreur serveur'}), 500

# Gérer le formulaire de contact
@app.route('/contact/', methods=['POST', 'OPTIONS'])
def contact():
    if request.method == 'OPTIONS':
        logging.info(f"Requête OPTIONS reçue de {request.headers.get('Origin')}")
        response = jsonify({'message': 'OK'})
        response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin'))
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')
            csrf_token = data.get('csrf_token')

            if not all([name, email, message, csrf_token]):
                logging.warning("Données manquantes dans la requête POST /contact/")
                return jsonify({'message': 'Tous les champs sont requis'}), 400

            with sqlite3.connect('messages.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO messages (name, email, message) VALUES (?, ?, ?)
                ''', (name, email, message))
                conn.commit()
            logging.info(f"Message enregistré : {name}, {email}")

            return jsonify({'message': 'Message reçu avec succès !'}), 200
        except Exception as e:
            logging.error(f"Erreur lors du traitement de la requête POST /contact/ : {e}")
            return jsonify({'message': 'Erreur serveur'}), 500

if __name__ == '__main__':
    logging.info("Démarrage du serveur Flask...")
    app.run(debug=True, host='0.0.0.0', port=5000)
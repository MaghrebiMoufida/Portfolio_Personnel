Portfolio Personnel - Développeuse IA, Mobile & Web
Ce projet est un portfolio personnel mettant en avant mes compétences en intelligence artificielle, développement mobile avec Flutter, et développement web avec Flask. Il présente mes projets, mes compétences techniques, et inclut un formulaire de contact interactif avec un backend Flask et une base de données SQLite.
Aperçu
Ce portfolio est une application web statique avec un frontend en HTML, CSS et JavaScript, et un backend Flask pour gérer les messages envoyés via le formulaire de contact. Les messages sont stockés dans une base de données SQLite. Le design est responsive et utilise Font Awesome pour les icônes et une mise en page moderne.
Compétences mises en avant

Langages : Java, Python, C, C++, C#, JavaScript, PHP, XML
Frameworks & Bibliothèques : Flutter, GetX, Flask, ASP.NET, TensorFlow, Keras
Intelligence Artificielle : Conception de modèles CNN (MobileNetV2), classification d’images
Bases de données : MongoDB, SQLite
Outils : Git, Visual Studio, VS Code, Google Colab
Méthodologies : Agile (Scrum)

Fonctionnalités

À propos : Présentation de mon parcours et de mes compétences.
Compétences : Grille visuelle des technologies maîtrisées avec icônes Font Awesome.
Projets : Showcase de projets, comme une application Flutter pour la classification de feuilles d’olivier et un portfolio avec backend Flask.
Contact : Formulaire interactif pour envoyer des messages, avec validation CSRF et stockage en base de données SQLite.
Responsive Design : Adapté aux écrans mobiles et desktops.

Prérequis

Python : Version 3.8 ou supérieure
Node.js : (Optionnel, pour un serveur local alternatif)
Navigateur web : Chrome, Firefox, ou tout autre navigateur moderne
Git : Pour cloner le dépôt

Installation

Cloner le dépôt :
git clone https://github.com/MaghrebiMoufida/Portfolio_Personnel.git
cd portfolio


Configurer le backend :

Navigue vers le dossier Backend :cd Backend


Installe les dépendances Python :pip install flask flask-cors


Lance le serveur Flask :python app.py


Le serveur démarre sur http://localhost:5000.


Configurer le frontend :

Retourne au dossier racine du projet.
Lance un serveur local pour servir les fichiers HTML, CSS, et JavaScript :
Avec Python :python -m http.server 8000

Accède à http://localhost:8000 dans ton navigateur.
Avec VS Code Live Server :
Ouvre le dossier dans VS Code.
Clique sur "Go Live" (extension Live Server, port généralement 5500).




Assure-toi que le port du frontend (par exemple, 8000 ou 5500) est autorisé dans la configuration CORS de app.py.


Vérifier la base de données :

Une base de données SQLite (messages.db) est automatiquement créée dans le dossier Backend pour stocker les messages du formulaire.



Utilisation

Ouvre le portfolio dans ton navigateur (par exemple, http://localhost:8000).
Explore les sections À propos, Compétences, et Projets.
Utilise le formulaire de contact pour envoyer un message :
Les messages sont envoyés au backend Flask et stockés dans messages.db.
Un message de confirmation ou d'erreur s'affiche après soumission.


Vérifie les logs dans le terminal Flask pour les requêtes (GET /csrf-token, POST /contact/) et les messages enregistrés.

Structure du projet
portfolio/
├── Backend/
│   ├── app.py              # Backend Flask
│   ├── messages.db         # Base de données SQLite (créée automatiquement)
├── index.html              # Page principale du portfolio
├── style.css               # Styles CSS
├── main.js                 # Logique JavaScript pour le formulaire
└── README.md               # Ce fichier

Débogage

Logs Flask : Vérifie les logs dans le terminal où app.py s'exécute pour diagnostiquer les erreurs.
Console du navigateur : Ouvre les outils de développement (F12 → Console/Network) pour voir les requêtes et erreurs JavaScript.
Problèmes CORS : Si des erreurs CORS apparaissent, ajuste les origines dans app.py :CORS(app, resources={r"/*": {"origins": ["http://localhost:<ton-port>"]}})


Port occupé : Si le port 5000 est utilisé, tue le processus :
Windows : netstat -aon | findstr :5000 puis taskkill /PID <numero> /F
Linux/Mac : lsof -i :5000 puis kill -9 <numero>



Contribution
Les contributions ou suggestions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request sur GitHub.
Contact

Email : moufidamaghrebi2016@gmail.com
GitHub : https://github.com/MaghrebiMoufida
Formulaire : Utilise le formulaire de contact sur le portfolio pour me joindre directement.

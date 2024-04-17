# backend/app.py
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from network_security import monitor_network_security


# Appeler la fonction pour obtenir les données de surveillance de la sécurité du réseau
#security_data = monitor_network_security()

# Afficher les données récupérées
#print("Intrusion detected:", security_data['intrusion_detected'])
#print("Log analysis result:", security_data['log_analysis_result'])

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
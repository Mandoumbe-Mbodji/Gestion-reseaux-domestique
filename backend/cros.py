# backend/app.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Autoriser toutes les origines

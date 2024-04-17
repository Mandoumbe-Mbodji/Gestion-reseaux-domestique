# backend/app.py
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app) # Autoriser toutes les origines
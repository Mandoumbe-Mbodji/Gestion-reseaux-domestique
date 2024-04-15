# backend/run.py
from app import app
from flask import jsonify
@app.route('/')
def index():
    return 'Bienvenue sur la page d\'accueil !'

# Route pour récupérer la liste des périphériques
@app.route('/devices')
def get_devices():
    devices = [
        {'name': 'Device 1', 'ip_address': '192.168.1.1'},
        {'name': 'Device 2', 'ip_address': '192.168.1.2'},
        {'name': 'Device 3', 'ip_address': '192.168.1.3'}
    ]
    return jsonify(devices)


if __name__ == '__main__':
   # app.run(debug=True)    
    app.run()
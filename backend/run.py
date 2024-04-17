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
        {'name': 'Device 2', 'ip_address': '192.168.1.0'},
        {'name': 'Device 3', 'ip_address': '192.168.1.3'}
    ]
    #return jsonify(devices)
    response = jsonify(devices)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8000')
    return response


if __name__ == '__main__':
   # app.run(debug=True)    
    app.run()
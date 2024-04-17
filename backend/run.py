from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices.db'
db = SQLAlchemy(app)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)

@app.route('/devices', methods=['GET', 'POST'])
def manage_devices():
    if request.method == 'GET':
        devices = Device.query.all()
        device_list = [{'id': device.id, 'name': device.name, 'ip_address': device.ip_address} for device in devices]
        return jsonify(device_list)
    elif request.method == 'POST':
        data = request.json
        name = data.get('name')
        ip_address = data.get('ip_address')
        if not name or not ip_address:
            return jsonify({'message': 'Name and IP address are required'}), 400
        new_device = Device(name=name, ip_address=ip_address)
        db.session.add(new_device)
        db.session.commit()
        return jsonify({'message': 'Device added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)

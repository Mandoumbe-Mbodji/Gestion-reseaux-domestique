# backend/resources.py
from flask_restful import Resource, reqparse
from models import Device

class DeviceListResource(Resource):
    def get(self):
        devices = Device.query.all()
        return [{'id': device.id, 'name': device.name, 'ip_address': device.ip_address} for device in devices]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name of the device is required')
        parser.add_argument('ip_address', type=str, required=True, help='IP address of the device is required')
        args = parser.parse_args()
        device = Device(name=args['name'], ip_address=args['ip_address'])
        db.session.add(device)
        db.session.commit()
        return {'message': 'Device added successfully'}, 201

api.add_resource(DeviceListResource, '/devices')

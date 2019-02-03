from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
api = Api(app)
app.secret_key = 'ducpa'

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with the name {} already exists.".format(name)}, 400

        data_request = request.get_json()
        item = {'name': name, 'price': data_request['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        for item in items:
            if item['name'] == name:
                items.remove(item)
                return {'message:', 'An item with the name {} had deleted'.format(name)}
        return {'item:', 'not found'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help="This field you type must be float")
        data_request = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data_request['price']}
            items.append(item)
        else:
            item.update(data_request)
        return item


class ItemList(Resource):
    def get(self):
        return items



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)


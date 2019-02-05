from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


stores = [
    {
        'name': 'my store',
        'items': [
            {
                'name': 'my item',
                'price': 10.9
            }
        ]
    }
]

# GET /store
@app.route('/store')
def get_store():
    return jsonify({'stores': stores})



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message':'store not found'})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})







if __name__ == '__main__':
    app.run(debug=True)

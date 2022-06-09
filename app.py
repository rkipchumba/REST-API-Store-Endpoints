from flask import Flask 

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name':'my item', 
            'price': 15.99 
            }
        ]
    }
]


#POST - used to receive data
#GET - used to send data back only

#post /store data: {name :}
@app.route("/store", methods=["POST"])
def create_store():
    pass

#get /store/<name> data: {name :}
@app.route("/store/<string:name>")
def get_store(name):
    pass

#get /store
@app.route("/store")
def get_stores():
    pass


#POST /store/<name> data: {name :}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass


#get /store/<name>/item data: {name :}
@app.route("/store/<string:name>/item")
def get_item_in_store():
    pass


app.run(port=5000)
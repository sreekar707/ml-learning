from flask import Flask,jsonify,request

app=Flask(__name__)

## initial data in my to do list
items=[
    {"id": 1,"name":"bag","description" : "this is the item bag"},
    {"id": 2,"name": "laptop","description" : "this is the item laptop"}
]


@app.route('/')
def home():
    return "Welcome to the Sample to do list app "


## get: retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)


## get : retrieve a specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error the item is not found"})
    return jsonify (item)

## post create a new task


@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error" :"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1, 
        "name": request.json['name'],
        "description":request.json['description']
    }
    
    
    items.append(new_item)
    return jsonify(new_item)

## updating 
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item ["id"]==item_id),None)
    if item is None:
        return jsonify ({"error" : "item not found"})
    item['name']= request.json.get('name',item['name'])
    item['description']= request.json.get('description',item['description'])
    return jsonify (item)


## deleting an item

@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item ["id"] != item_id]
    return jsonify ({"results": "item deleted"})
if(__name__=="__main__"):
    app.run(debug=True)
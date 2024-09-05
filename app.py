from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt
from db import read_items, write_items
from typing import Annotated

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world() -> str:
    return "Hello World!"

@app.route('/grocery_items', methods=['GET'])
def get_grocery_items() -> jsonify:
    try:
        grocery_items = read_items()
        items = [{"id": item["id"], "name": item["name"], "price": item["price"]} for item in grocery_items]
        return jsonify(items)
    except Exception as e:
        # Provide detailed traceback information for debugging
        import traceback
        e.add_note("Error occurred while fetching grocery items.")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/grocery_items', methods=['POST'])
def add_grocery_item() -> tuple[str, int]:
    try:
        new_item = request.json
        print(new_item["id"], new_item, flush=True)
        grocery_items = read_items()
        if new_item not in grocery_items:
            grocery_items.append(new_item)
            write_items(grocery_items)
        return "Successfully added item", 201
    except Exception as e:
        # Provide detailed traceback information for debugging
        import traceback
        e.add_note("Error occurred while adding a new grocery item.")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/grocery_items/<int:item_id>', methods=['DELETE'])
def delete_grocery_item(item_id: int) -> tuple[str, int]:
    try:
        grocery_items = read_items()
        grocery_items = [item for item in grocery_items if item["id"] != item_id]
        write_items(grocery_items)
        return "Successfully deleted item", 200
    except Exception as e:
        # Provide detailed traceback information for debugging
        import traceback
        e.add_note("Error occurred while deleting a grocery item.")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/hashpassword/<Annotated[str, "password"]>', methods=['GET'])
def hash_password(password: Annotated[str, "password"]) -> str:
    try:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    except Exception as e:
        # Provide detailed traceback information for debugging
        import traceback
        e.add_note("Error occurred while hashing the password.")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True)

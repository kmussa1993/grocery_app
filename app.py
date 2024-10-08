from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt
from db import read_items, write_items

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """ 
    Returns a simple greeting message.

    Returns:
        str: A greeting message "Hello World!".
    """
    return "Hello World!"

@app.route('/grocery_items', methods=['GET'])
def get_grocery_items():
    """ 
    Retrieves a list of grocery items.

    This method reads grocery items from the database and formats them into a 
    list of dictionaries containing the id, name, and price of each item.

    Returns:
        json: A JSON response containing a list of grocery items.
        If an error occurs, returns a 500 status code with the error message.
    """
    try:
        grocery_items = read_items()  # Read items from the database
        items = [{"id": item["id"], "name": item["name"], "price": item["price"]} for item in grocery_items]
        return jsonify(items)  # Return the list of items as JSON
    except Exception as e:
        return e, 500  # Return error message with 500 status code

@app.route('/grocery_items', methods=['POST'])
def add_grocery_item():
    """ 
    Adds a new grocery item to the database.

    This method expects a JSON payload containing the new item details. 
    If the item does not already exist in the database, it appends the item 
    to the list and writes the updated list back to the database.

    Returns:
        str: A success message indicating the item was added.
        int: HTTP status code 201 if successful.
        If an error occurs, returns a 500 status code with the error message.
    """
    try:
        new_item = request.json  # Get the new item from the request
        print(new_item["id"], new_item, flush=True)  # Log the new item for debugging
        grocery_items = read_items()  # Read existing items from the database
        if new_item not in grocery_items:  # Check if the item already exists
            grocery_items.append(new_item)  # Add the new item to the list
            write_items(grocery_items)  # Write the updated list back to the database
        return "Successfully added item", 201  # Return success message
    except Exception as e:
        return e, 500  # Return error message with 500 status code
    
@app.route('/grocery_items/<int:item_id>', methods=['DELETE'])
def delete_grocery_item(item_id):
    """ 
    Deletes a grocery item from the database.

    This method removes the item with the specified item_id from the database 
    and writes the updated list back to the database.

    Args:
        item_id (int): The ID of the grocery item to be deleted.

    Returns:
        str: A success message indicating the item was deleted.
        int: HTTP status code 200 if successful.
        If an error occurs, returns a 500 status code with the error message.
    """
    try:
        grocery_items = read_items()  # Read existing items from the database
        grocery_items = [item for item in grocery_items if item["id"] != item_id]  # Filter out the item to delete
        write_items(grocery_items)  # Write the updated list back to the database
        return "Successfully deleted item", 200  # Return success message
    except Exception as e:
        return e, 500  # Return error message with 500 status code

@app.route('/hashpassword/<string:password>', methods=['GET'])
def hash_password(password):
    """ 
    Hashes a given password using bcrypt.

    This method takes a password as input and returns its hashed version.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
        If an error occurs, returns a 500 status code with the error message.
    """
    try:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')  # Return the hashed password
    except Exception as e:
        return e, 500  # Return error message with 500 status code

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
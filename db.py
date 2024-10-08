import json

def read_items():
    """
    Reads grocery items from a JSON file.

    This function opens the 'storage/items.json' file, loads its content
    as a JSON object, and returns it as a Python dictionary.

    Returns:
        dict: A dictionary containing grocery items loaded from the JSON file.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)  # Load JSON data from the file
    return grocery_items  # Return the loaded grocery items

def write_items(grocery_items):
    """
    Writes grocery items to a JSON file.

    This function takes a dictionary of grocery items and writes it to
    the 'storage/items.json' file in JSON format.

    Args:
        grocery_items (dict): A dictionary containing grocery items to be saved.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)  # Dump the dictionary as JSON into the file
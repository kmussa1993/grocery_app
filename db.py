import json

def read_items():
    try:
        with open('storage/items.json') as f:
            grocery_items = json.load(f)
        return grocery_items
    except* (FileNotFoundError, json.JSONDecodeError) as e:
        if isinstance(e, FileNotFoundError):
            raise FileNotFoundError(f"Error: {e}. The file 'storage/items.json' was not found.")
        elif isinstance(e, json.JSONDecodeError):
            raise json.JSONDecodeError(f"Error: {e}. Failed to decode JSON from 'storage/items.json'.")

def write_items(grocery_items):
    try:
        with open('storage/items.json', 'w') as f:
            json.dump(grocery_items, f)
    except IOError as e:
        raise IOError(f"Error: {e}. Failed to write to 'storage/items.json'.")

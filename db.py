import json
from typing import TypeVar, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class GroceryItem:
    # Assuming the structure of the grocery item, you can add fields here
    # For example: name: str, quantity: int, price: float
    pass

def read_items() -> List[GroceryItem]:
    try:
        with open('storage/items.json') as f:
            grocery_items_data = json.load(f)
            grocery_items = [GroceryItem(**item) for item in grocery_items_data]
        return grocery_items
    except (FileNotFoundError, json.JSONDecodeError) as e:
        if isinstance(e, FileNotFoundError):
            e.add_note("The file 'storage/items.json' was not found.")
            raise
        elif isinstance(e, json.JSONDecodeError):
            e.add_note("Failed to decode JSON from 'storage/items.json'.")
            raise

def write_items(grocery_items: List[GroceryItem]) -> None:
    try:
        with open('storage/items.json', 'w') as f:
            grocery_items_data = [item.__dict__ for item in grocery_items]
            json.dump(grocery_items_data, f)
    except IOError as e:
        e.add_note("Failed to write to 'storage/items.json'.")
        raise

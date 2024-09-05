import json
from typing import TypeVar, List

T = TypeVar('T')

def read_items() -> List[T]:
    try:
        with open('storage/items.json') as f:
            grocery_items = json.load(f)
        return grocery_items
    except (FileNotFoundError, json.JSONDecodeError) as e:
        if isinstance(e, FileNotFoundError):
            e.add_note("The file 'storage/items.json' was not found.")
            raise
        elif isinstance(e, json.JSONDecodeError):
            e.add_note("Failed to decode JSON from 'storage/items.json'.")
            raise

def write_items(grocery_items: List[T]) -> None:
    try:
        with open('storage/items.json', 'w') as f:
            json.dump(grocery_items, f)
    except IOError as e:
        e.add_note("Failed to write to 'storage/items.json'.")
        raise

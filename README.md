# Grocery Item Management System

Welcome to the Grocery Item Management System! This directory contains the essential components for managing grocery items using a simple Flask application. Below is a brief overview of the key files in this module.

## Files Overview

### 1. `db.py`
- **Description**: This module provides functions for managing grocery items stored in a JSON file.
- **Functions**:
  - `read_items()`: Reads and returns grocery items as a Python dictionary from `storage/items.json`.
  - `write_items(items: dict)`: Takes a dictionary of grocery items and writes it back to the `storage/items.json` file.
- **Documentation**: Each function is well-documented, explaining its purpose, parameters, and return values.

### 2. `app.py`
- **Description**: This is the main Flask application that serves as a simple grocery item management system.
- **Features**:
  - Greeting users
  - Retrieving grocery items
  - Adding new items
  - Deleting items by ID
  - Hashing passwords
- **Functionality**: The application interacts with the `db.py` module to read and write grocery items, ensuring that items are unique when added.
- **Documentation**: Each route is well-documented, detailing the expected inputs, outputs, and error handling, making it easy for developers to understand and extend the functionality.

## Getting Started

To get started with the Grocery Item Management System, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Flask installed. You can install it using pip:
   ```bash
   pip install Flask
   ```
3. **Run the Application**: Start the Flask application by running:
   ```bash
   python app.py
   ```
4. **Access the API**: Open your web browser or use a tool like Postman to interact with the API endpoints.

## Contributing

We welcome contributions to enhance the functionality of the Grocery Item Management System. Please ensure that your code is well-documented and follows the existing coding style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code and make modifications as needed. Happy coding!
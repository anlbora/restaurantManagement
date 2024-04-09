import sqlite3
from PyQt5.QtWidgets import QMessageBox
import plotly.graph_objects as go

class Product:
    def __init__(self, table_name):
        """
        Initializes the Product class.

        Establishes a connection to the SQLite database and creates the specified table if it doesn't exist.

        Args:
            table_name (str): The name of the table to be created or accessed in the SQLite database.
        
        Returns:
            None
        """
        self.table_name = table_name
        self.conn = sqlite3.connect('Restaurant.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates a new table in the SQLite database if it doesn't exist.

        Defines the table schema with columns for ID, name, price, and ingredients.

        Args:
            None

        Returns:
            None
        """
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                ingredients TEXT
            )
        ''')
        self.conn.commit()

    def add_product(self, name, price, ingredients):
        """
        Adds a new product to the database table.

        Inserts a new row with the specified name, price, and ingredients into the database table.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            ingredients (str): The ingredients used in the product.

        Returns:
            None
        """
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, price, ingredients) VALUES (?, ?, ?)", (name, price, ingredients ))
        self.conn.commit()
        QMessageBox.information(None, "Success", f"{name} was added.")

    def delete_product(self, product_id):
        """
        Deletes a product from the database table by ID.

        Removes the product with the specified ID from the database table.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            None
        """
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (product_id,))
        self.conn.commit()
        QMessageBox.information(None, "Success", f"The product with {product_id} was deleted.")

    def update_product(self, product_id, name, price, ingredients):
        """
        Updates a product in the database table by ID.

        Modifies the name, price and ingredients of the product with the specified ID in the database table.

        Args:
            product_id (int): The ID of the product to be updated.
            name (str): The new name of the product.
            price (float): The new price of the product.
            ingredients (str): Ingredients of the product.

        Returns:
            None
        """
        self.cursor.execute(f"UPDATE {self.table_name} SET name=?, price=?, ingredients = ? WHERE id=?", (name, price, ingredients, product_id))
        self.conn.commit()
        QMessageBox.information(None, "Success", f"The product with {product_id} was updated.")

    def show_products(self):
        """
        Fetches and displays the products from the database in an interactive table using Plotly.

        Retrieves product data from the specified table in the database, 
        creates a table representation using Plotly, 
        and displays it interactively.

        Args:
            self: The instance of the Product class.

        Returns:
            None
        """
        
        # Execute SQL query to fetch product data
        self.cursor.execute(f"SELECT id, name, price, ingredients FROM {self.table_name}")
        
        # Fetch all products
        products = self.cursor.fetchall()

        # Extract data for the table
        ids = [product[0] for product in products]  # List of product IDs
        names = [product[1] for product in products]  # List of product names
        prices = [product[2] for product in products]  # List of product prices
        ingredients = [product[3] for product in products]  # List of product ingredients

        # Create a table using Plotly
        fig = go.Figure(data=[go.Table(
            header=dict(values=['ID', 'Name', 'Price', 'Ingredients']),  # Table headers
            cells=dict(values=[ids, names, prices, ingredients]))  # Table data
        ])

        # Set layout and title for the table
        fig.update_layout(title=f"Products in {self.table_name.upper()}")

        # Display the table interactively
        fig.show()
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import plotly.graph_objects as go

class Orders:
    def __init__(self):
        """
        Initializes the Orders class.

        Establishes a connection to the SQLite database and creates the Orders table if it doesn't exist.

        Args:
            None
        
        Returns:
            None
        """
        self.conn = sqlite3.connect('Restaurant.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the Orders table in the SQLite database if it doesn't exist.

        Defines the table schema with columns for ID, food ID, drink ID, food quantity, drink quantity, total price,
        and foreign keys to reference the Foods and Drinks tables.

        Args:
            None

        Returns:
            None
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_id INTEGER NOT NULL,
                drink_id INTEGER NOT NULL,
                food_quantity INTEGER NOT NULL,
                drink_quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                notes TEXT,
                FOREIGN KEY (food_id) REFERENCES Foods(id),
                FOREIGN KEY (drink_id) REFERENCES Drinks(id)
            )
        ''')
        self.conn.commit()

    def take_order(self, food_id, drink_id, food_quantity, drink_quantity, notes):
        """
        Takes a new order and calculates the total price.

        Inserts a new order with the specified food and drink IDs, quantities, and total price into the Orders table.

        Args:
            food_id (int): The ID of the food product.
            drink_id (int): The ID of the drink product.
            food_quantity (int): The quantity of the food product.
            drink_quantity (int): The quantity of the drink product.
            notes (str): Notes about the order.

        Returns:
            None
        """
        food_price = self.get_product_price('Foods', food_id)
        drink_price = self.get_product_price('Drinks', drink_id)
        total_price = (food_price * food_quantity) + (drink_price * drink_quantity)
        
        self.cursor.execute("INSERT INTO Orders (food_id, drink_id, food_quantity, drink_quantity, total_price, notes) VALUES (?, ?, ?, ?, ?, ?)",
                            (food_id, drink_id, food_quantity, drink_quantity, total_price, notes))
        self.conn.commit()

        msg = f"{food_quantity} {self.get_product_name('Foods', food_id)} and {drink_quantity} {self.get_product_name('Drinks', drink_id)} were ordered. Total Price: {total_price} $ \n Notes about the Order: {notes}"
        self.show_message("Order was taken", msg)

    def show_orders(self):
        """
        Displays all orders from the Orders table using Plotly's interactive table.
        
        Fetches all orders from the Orders table and displays them in an interactive table.

        Args:
            None

        Returns:
            None
        """
        self.cursor.execute('''
            SELECT Orders.id, Foods.name AS Food, Drinks.name AS Drink, 
            Orders.food_quantity, Orders.drink_quantity, Orders.total_price AS TotalPrice, Orders.notes AS Notes
            FROM Orders
            INNER JOIN Foods ON Orders.food_id = Foods.id
            INNER JOIN Drinks ON Orders.drink_id = Drinks.id
        ''')
        orders = self.cursor.fetchall()

        if not orders:
            self.show_message("Warning", "There are no orders yet.")
        else:
            order_dict = {
                "ID": [order[0] for order in orders],
                "Food": [order[1] for order in orders],
                "Drink": [order[2] for order in orders],
                "Food Quantity": [order[3] for order in orders],
                "Drink Quantity": [order[4] for order in orders],
                "Total Price": [order[5] for order in orders],
                "Notes": [order[6] for order in orders]
            }

            fig = go.Figure(data=[go.Table(
                header=dict(values=["ID", "Food", "Drink", "Food Quantity", "Drink Quantity", "Total Price", "Notes"]),
                cells=dict(values=[order_dict["ID"], order_dict["Food"], order_dict["Drink"], 
                                order_dict["Food Quantity"], order_dict["Drink Quantity"], 
                                order_dict["Total Price"], order_dict["Notes"]]))
            ])

            fig.show()

    def get_product_price(self, table, product_id):
        """
        Retrieves the price of a product from the specified table.

        Fetches the price of a product with the given ID from the specified table.

        Args:
            table (str): The name of the table to retrieve the product price from.
            product_id (int): The ID of the product.

        Returns:
            float: The price of the product.
        """
        self.cursor.execute(f"SELECT price FROM {table} WHERE id=?", (product_id,))
        price = self.cursor.fetchone()
        if price:
            return price[0]
        else:
            #self.show_message("Warning", "Product doesn't exist.")
            return 0

    def get_product_name(self, table, product_id):
        """
        Retrieves the name of a product from the specified table.

        Fetches the name of a product with the given ID from the specified table.

        Args:
            table (str): The name of the table to retrieve the product name from.
            product_id (int): The ID of the product.

        Returns:
            str: The name of the product.
        """
        self.cursor.execute(f"SELECT name FROM {table} WHERE id=?", (product_id,))
        name = self.cursor.fetchone()
        if name:
            return name[0]
        else:
            #self.show_message("Warning", "Product doesn't exist.")
            return ""
    
    def get_product_id(self, table, name):
        """
        Retrieves the ID of a product from the specified table.

        Fetches the ID of a product with the given name from the specified table.

        Args:
            table (str): The name of the table to retrieve the product ID from.
            name (str): The name of the product.

        Returns:
            int: The ID of the product.
        """
        self.cursor.execute(f"SELECT id FROM {table} WHERE name=?", (name,))
        id = self.cursor.fetchone()
        if id:
            return id[0]
        else:
            #self.show_message("Warning", "Product doesn't exist.")
            return ""

    def show_message(self, title, message):
        """
        Displays a message box with the specified title and message.

        Creates and displays a message box with the given title and message using PyQt5's QMessageBox.

        Args:
            title (str): The title of the message box.
            message (str): The message to display in the message box.

        Returns:
            None
        """
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

from Food import *
from Drink import *
from Orders import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 900)
        MainWindow.setMinimumSize(QtCore.QSize(710, 900))
        MainWindow.setMaximumSize(QtCore.QSize(710, 900))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 241, 861))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 821))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_addFood = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_addFood.setFont(font)
        self.btn_addFood.setObjectName("btn_addFood")
        self.verticalLayout.addWidget(self.btn_addFood)
        self.btn_deleteFood = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_deleteFood.setFont(font)
        self.btn_deleteFood.setObjectName("btn_deleteFood")
        self.verticalLayout.addWidget(self.btn_deleteFood)
        self.btn_updateFood = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_updateFood.setFont(font)
        self.btn_updateFood.setObjectName("btn_updateFood")
        self.verticalLayout.addWidget(self.btn_updateFood)
        self.btn_showFoods = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_showFoods.setFont(font)
        self.btn_showFoods.setObjectName("btn_showFoods")
        self.verticalLayout.addWidget(self.btn_showFoods)
        self.btn_addDrink = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_addDrink.setFont(font)
        self.btn_addDrink.setObjectName("btn_addDrink")
        self.verticalLayout.addWidget(self.btn_addDrink)
        self.btn_deleteDrink = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_deleteDrink.setFont(font)
        self.btn_deleteDrink.setObjectName("btn_deleteDrink")
        self.verticalLayout.addWidget(self.btn_deleteDrink)
        self.btn_updateDrink = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_updateDrink.setFont(font)
        self.btn_updateDrink.setObjectName("btn_updateDrink")
        self.verticalLayout.addWidget(self.btn_updateDrink)
        self.btn_showDrinks = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_showDrinks.setFont(font)
        self.btn_showDrinks.setObjectName("btn_showDrinks")
        self.verticalLayout.addWidget(self.btn_showDrinks)
        self.btn_order = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_order.setFont(font)
        self.btn_order.setObjectName("btn_order")
        self.verticalLayout.addWidget(self.btn_order)
        self.btn_showOrders = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_showOrders.setFont(font)
        self.btn_showOrders.setObjectName("btn_showOrders")
        self.verticalLayout.addWidget(self.btn_showOrders)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(259, 9, 441, 861))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 421, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_food = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_food.setFrame(False)
        self.name_food.setObjectName("name_food")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_food)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.price_food = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price_food.setFrame(False)
        self.price_food.setObjectName("price_food")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.price_food)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ingredients_food = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.ingredients_food.setObjectName("ingredients_food")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ingredients_food)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 421, 241))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.name_drink = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.name_drink.setFrame(False)
        self.name_drink.setObjectName("name_drink")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_drink)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.price_drink = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.price_drink.setFrame(False)
        self.price_drink.setObjectName("price_drink")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.price_drink)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.ingredients_drink = QtWidgets.QTextEdit(self.formLayoutWidget_3)
        self.ingredients_drink.setObjectName("ingredients_drink")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ingredients_drink)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(9, 29, 421, 241))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.orders_foodId = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.orders_foodId.setFrame(False)
        self.orders_foodId.setObjectName("orders_foodId")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.orders_foodId)
        self.orders_drinkId = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.orders_drinkId.setFrame(False)
        self.orders_drinkId.setObjectName("orders_drinkId")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.orders_drinkId)
        self.orders_foodQuantity = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.orders_foodQuantity.setFrame(False)
        self.orders_foodQuantity.setObjectName("orders_foodQuantity")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.orders_foodQuantity)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.orders_drinkQuantity = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.orders_drinkQuantity.setFrame(False)
        self.orders_drinkQuantity.setObjectName("orders_drinkQuantity")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.orders_drinkQuantity)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.orders_notes = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.orders_notes.setObjectName("orders_notes")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.orders_notes)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_addFood.clicked.connect(self.addFood)
        self.btn_showFoods.clicked.connect(self.showAllFoods)
        self.btn_updateFood.clicked.connect(self.updateFood)
        self.btn_deleteFood.clicked.connect(self.deleteFood)

        self.btn_addDrink.clicked.connect(self.addDrink)
        self.btn_showDrinks.clicked.connect(self.showAllDrinks)
        self.btn_updateDrink.clicked.connect(self.updateDrink)
        self.btn_deleteDrink.clicked.connect(self.deleteDrink)

        self.btn_order.clicked.connect(self.takeOrder)
        self.btn_showOrders.clicked.connect(self.showAllOrders)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WELCOME TO RESTAURANT MANAGEMENT SYSTEM"))
        self.groupBox.setTitle(_translate("MainWindow", "Menu"))
        self.btn_addFood.setText(_translate("MainWindow", "Add Food"))
        self.btn_deleteFood.setText(_translate("MainWindow", "Delete Food"))
        self.btn_updateFood.setText(_translate("MainWindow", "Update Food"))
        self.btn_showFoods.setText(_translate("MainWindow", "Show Foods"))
        self.btn_addDrink.setText(_translate("MainWindow", "Add Drink"))
        self.btn_deleteDrink.setText(_translate("MainWindow", "Delete Drink"))
        self.btn_updateDrink.setText(_translate("MainWindow", "Update Drink"))
        self.btn_showDrinks.setText(_translate("MainWindow", "Show Drinks"))
        self.btn_order.setText(_translate("MainWindow", "Order"))
        self.btn_showOrders.setText(_translate("MainWindow", "Show Orders"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Foods"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Price:"))
        self.label_3.setText(_translate("MainWindow", "Ingredients:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Drinks"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Price:"))
        self.label_6.setText(_translate("MainWindow", "Ingredients:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Orders"))
        self.label_7.setText(_translate("MainWindow", "Food Name:"))
        self.label_8.setText(_translate("MainWindow", "Drink Name:"))
        self.label_9.setText(_translate("MainWindow", "Food Quantity:"))
        self.label_10.setText(_translate("MainWindow", "Drink Quantity:"))
        self.label_11.setText(_translate("MainWindow", "Notes:"))

    def addFood(self):
        """
        Method to add a new food product to the database.
        
        This method retrieves the food name, price, and ingredients entered by the user 
        from the respective input fields in the GUI. It then calls the 'add_product' method 
        from the Food class to add the new food to the database.
        
        Returns:
            None
        
        Raises:
            ValueError: If the price entered is not an integer.
        """
        
        try:
            # Retrieve food details from GUI input fields
            name = self.name_food.text()
            price = int(self.price_food.text())
            ingredients = self.ingredients_food.toPlainText()

            # Initialize Food object
            food = Food()
            
            # Add new food product
            food.add_product(name, price, ingredients)
            self.clearFoodFields()
        
        except ValueError:
            # Handle ValueError if the price entered is not an integer
            QMessageBox.information(None, "Error", "Please enter a valid price. Price should be an integer.")
            
    def showAllFoods(self):
        """
        Method to display all food products from the database.
        
        This method calls the 'show_products' method from the Food class to retrieve 
        and display all food products from the database.
        
        Returns:
            None
        """
        
        # Initialize Food object
        food = Food()
        
        # Display all food products
        food.show_products()
        
    def updateFood(self):
        """
        Method to update an existing food product in the database.
        
        This method retrieves the food name, price, and ingredients entered by the user 
        from the respective input fields in the GUI. It then calls the 'get_product_id' 
        method from the Orders class to fetch the product ID. Finally, it calls the 
        'update_product' method from the Food class to update the food product in the database.
        
        Returns:
            None
        
        Raises:
            ValueError: If the price entered is not an integer.
            KeyError: If the food name entered is not found in the database.
        """
        
        try:
            # Retrieve food details from GUI input fields
            name = self.name_food.text()
            price = int(self.price_food.text())
            ingredients = self.ingredients_food.toPlainText()

            # Initialize Orders object
            order = Orders()
            
            # Get product ID for the food
            product_id = order.get_product_id("Foods", name)

            # Initialize Food object
            food = Food()
            
            # Update food product
            food.update_product(product_id, name, price, ingredients)
            self.clearFoodFields()
        
        except ValueError:
            # Handle ValueError if the price entered is not an integer
            QMessageBox.information(None, "Error", "Please enter a valid price. Price should be an integer.")
            
        except KeyError as e:
            # Handle KeyError if the food name entered is not found in the database
            QMessageBox.information(None, "Error", "{e} not found in the database. Please enter a valid food name.")

    def deleteFood(self):
        """
        Method to delete an existing food product from the database.
        
        This method retrieves the food name entered by the user from the input field 
        in the GUI. It then calls the 'get_product_id' method from the Orders class to 
        fetch the product ID. Finally, it calls the 'delete_product' method from the 
        Food class to delete the food product from the database.
        
        Returns:
            None
        
        Raises:
            KeyError: If the food name entered is not found in the database.
        """
        
        try:
            # Retrieve food name from GUI input field
            name = self.name_food.text()

            # Initialize Orders object
            order = Orders()
            
            # Get product ID for the food
            product_id = order.get_product_id("Foods", name)

            # Initialize Food object
            food = Food()
            
            # Delete food product
            food.delete_product(product_id)
            self.clearFoodFields()
        
        except KeyError as e:
            # Handle KeyError if the food name entered is not found in the database
            QMessageBox.information(None, "Error", "{e} not found in the database. Please enter a valid food name.")
   
    def addDrink(self):
        """
        Method to add a new drink product to the database.
        
        This method retrieves the drink name, price, and ingredients entered by the user 
        from the respective input fields in the GUI. It then calls the 'add_product' method 
        from the Drink class to add the new drink to the database.
        
        Returns:
            None
        
        Raises:
            ValueError: If the price entered is not an integer.
        """
        
        try:
            # Retrieve drink details from GUI input fields
            name = self.name_drink.text()
            price = int(self.price_drink.text())
            ingredients = self.ingredients_drink.toPlainText()

            # Initialize Drink object
            drink = Drink()
            
            # Add new drink product
            drink.add_product(name, price, ingredients)
            self.clearDrinkFields()
        
        except ValueError:
            # Handle ValueError if the price entered is not an integer
            QMessageBox.information(None, "Error", "Please enter a valid price. Price should be an integer.")
            
    def showAllDrinks(self):
        """
        Method to display all drink products from the database.
        
        This method calls the 'show_products' method from the Drink class to retrieve 
        and display all drink products from the database.
        
        Returns:
            None
        """
        
        # Initialize Drink object
        drink = Drink()
        
        # Display all drink products
        drink.show_products()
        
    def updateDrink(self):
        """
        Method to update an existing drink product in the database.
        
        This method retrieves the drink name, price, and ingredients entered by the user 
        from the respective input fields in the GUI. It then calls the 'get_product_id' 
        method from the Orders class to fetch the product ID. Finally, it calls the 
        'update_product' method from the Drink class to update the drink product in the database.
        
        Returns:
            None
        
        Raises:
            ValueError: If the price entered is not an integer.
            KeyError: If the drink name entered is not found in the database.
        """
        
        try:
            # Retrieve drink details from GUI input fields
            name = self.name_drink.text()
            price = int(self.price_drink.text())
            ingredients = self.ingredients_drink.toPlainText()

            # Initialize Orders object
            order = Orders()
            
            # Get product ID for the drink
            product_id = order.get_product_id("Drinks", name)

            # Initialize Drink object
            drink = Drink()
            
            # Update drink product
            drink.update_product(product_id, name, price, ingredients)
            self.clearDrinkFields()
        
        except ValueError:
            # Handle ValueError if the price entered is not an integer
            QMessageBox.information(None, "Error", "Please enter a valid price. Price should be an integer.")
            
        except KeyError as e:
            # Handle KeyError if the drink name entered is not found in the database
            QMessageBox.information(None, "Error", "{e} not found in the database. Please enter a valid drink name.")

    def deleteDrink(self):
        """
        Method to delete an existing drink product from the database.
        
        This method retrieves the drink name entered by the user from the input field 
        in the GUI. It then calls the 'get_product_id' method from the Orders class to 
        fetch the product ID. Finally, it calls the 'delete_product' method from the 
        Drink class to delete the drink product from the database.
        
        Returns:
            None
        
        Raises:
            KeyError: If the drink name entered is not found in the database.
        """
        
        try:
            # Retrieve drink name from GUI input field
            name = self.name_drink.text()

            # Initialize Orders object
            order = Orders()
            
            # Get product ID for the drink
            product_id = order.get_product_id("Drinks", name)

            # Initialize Drink object
            drink = Drink()
            
            # Delete drink product
            drink.delete_product(product_id)
            self.clearDrinkFields()
        
        except KeyError as e:
            # Handle KeyError if the drink name entered is not found in the database
            QMessageBox.information(None, "Error", "{e} not found in the database. Please enter a valid drink name.")

    def takeOrder(self):
        """
        Method to take customer orders from the GUI input fields.
        
        This method retrieves the food and drink names and quantities entered by the user 
        from the respective text input fields in the GUI. It then fetches the corresponding 
        product IDs using the 'get_product_id' method from the Orders class. Finally, it calls 
        the 'take_order' method to process the order with the fetched IDs and quantities.
        
        Returns:
            None
        
        Raises:
            ValueError: If the quantity entered is not an integer.
            KeyError: If the food or drink name entered is not found in the database.
        """
        
        try:
            # Retrieve food and drink names and quantities from GUI input fields
            food_name = self.orders_foodId.text()
            drink_name = self.orders_drinkId.text()
            food_qty = int(self.orders_foodQuantity.text())
            drink_qty = int(self.orders_drinkQuantity.text())
            notes = self.orders_notes.toPlainText()

            # Initialize Orders object
            order = Orders()
            
            # Get product IDs for food and drink
            food_id = order.get_product_id("Foods", food_name)
            drink_id = order.get_product_id("Drinks", drink_name)
            
            # Process the order
            order.take_order(food_id, drink_id, food_qty, drink_qty, notes)
            self.clearOrderFields()
            
        except ValueError:
            # Handle ValueError if the quantity entered is not an integer
            QMessageBox.information(None, "Error", "Please enter a valid quantity. Quantity should be an integer.")
            
        except KeyError as e:
            # Handle KeyError if the food or drink name entered is not found in the database
            QMessageBox.information(None, "Error", "{e} not found in the database. Please enter a valid drink name.")

    def showAllOrders(self):
        """
        Method to display all orders from the database.
        
        This method calls the 'show_orders' method from the Orders class to retrieve 
        and display all orders from the database.
        
        Returns:
            None
        """
        
        # Initialize Orders object
        order = Orders()
        
        # Display all orders
        order.show_orders()

    def clearFoodFields(self):
        """
        Clear the input fields related to food products in the GUI.
        
        This method clears the text input fields for adding or updating food products in the GUI.
        After calling this method, the 'name_food', 'price_food', and 'ingredients_food' fields 
        will be set to empty strings.

        Args:
            None

        Returns:
            None
        """
        self.name_food.setText("")
        self.price_food.setText("")
        self.ingredients_food.setText("")

    def clearDrinkFields(self):
        """
        Clear the input fields related to drink products in the GUI.
        
        This method clears the text input fields for adding or updating drink products in the GUI.
        After calling this method, the 'name_drink', 'price_drink', and 'ingredients_drink' fields 
        will be set to empty strings.

        Args:
            None

        Returns:
            None
        """
        self.name_drink.setText("")
        self.price_drink.setText("")
        self.ingredients_drink.setText("")

    def clearOrderFields(self):
        """
        Clear the input fields related to orders in the GUI.
        
        This method clears the text input fields for taking customer orders in the GUI.
        After calling this method, the 'orders_foodId', 'orders_drinkId', 'orders_foodQuantity', 
        'orders_drinkQuantity', and 'orders_notes' fields will be set to empty strings.

        Args:
            None

        Returns:
            None
        """
        self.orders_foodId.setText("")
        self.orders_drinkId.setText("")
        self.orders_foodQuantity.setText("")
        self.orders_drinkQuantity.setText("")
        self.orders_notes.setText("")



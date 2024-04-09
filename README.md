# Movie Management Program

## Overview

The Restaurant Management Program is a PyQt5-based desktop application designed to manage and organize information about orders, foods, and drinks to be used by user. It provides functionalities for adding, editing, deleting, and viewing orders, foods, drinks' details. The program utilizes an SQLite database to store and manage data.

## Features

### Main Window
Admin panel lets the admin do various types of actions on Users, Movies and Directors such as **View, Add, Update and Delete.** Admin Panel's methods have their own explanations in the code. All methods have exception handling not to break down the program. 

![1](https://github.com/anlbora/restaurantManagement/assets/100442507/42d53e76-2432-4891-838c-e0d44f6b78b4)
![2](https://github.com/anlbora/restaurantManagement/assets/100442507/ad08c70c-e20b-4cc4-975f-df370a678ccc)

### Food Management

- **View All Foods**: Displays a comprehensive list of all registered foods.
  ![4](https://github.com/anlbora/restaurantManagement/assets/100442507/8b4537d7-da12-4f05-bc18-178e64671c68)
- **Add Foods**: Enables the addition of new foods.
- **Update Foods**: Allows modification of existing food information.
- **Delete Foods**: Facilitates the removal of food.

### Drink Management

- **View All Drinks**: Presents a list of all registered drinks.
- **Add Drinks**: Allows the addition of new drinks.
- **Update Drinks**: Permits updates to existing drink details.
- **Delete Drinks**: Enables the deletion of drinks from the database.

### Order Management

- **View All Orders**: Displays a table containing information on all orders in the database.
  ![3](https://github.com/anlbora/restaurantManagement/assets/100442507/13d38ec6-cada-4960-8839-a527fabb4c7d)
- **Add Orders**: Facilitates the addition of new order entries.
  
## Requirements

- Python
- PyQt5
- SQLite3

## Installation

1. Clone the repository:
  - git clone https://github.com/yourusername/restaurantManagement.git
2. Navigate to the project directory:
  - cd restaurantManagement
3. Install the required dependencies:
  - pip install -r requirements.txt
4. Run the application:
  - python main.py


## Usage

1. Launch the application by running `main.py`.
2. Sign up for a new account or log in with an existing account.
3. Use the respective buttons in the MainWindow to manage foods, drinks, and orders.

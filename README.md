# Movie Management Program

## Overview

The Restaurant Management Program is a PyQt5-based desktop application designed to manage and organize information about orders, foods, and drinks to be used by user. It provides functionalities for adding, editing, deleting, and viewing orders, foods, drinks' details. The program utilizes an SQLite database to store and manage data.

## Features

### Main Window
Admin panel lets the admin do various types of actions on Users, Movies and Directors such as **View, Add, Update and Delete.** Admin Panel's methods have their own explanations in the code. All methods have exception handling not to break down the program. 

![1](https://github.com/anlbora/restaurantManagement/assets/100442507/42d53e76-2432-4891-838c-e0d44f6b78b4)

### Food Management

- **View All Foods**: Displays a comprehensive list of all registered users.
- **Add Foods**: Enables the addition of new user accounts.
- **Update Foods**: Allows modification of existing user information.
- **Delete Foods**: Facilitates the removal of user accounts after authentication.

### Drink Management

- **View All Drinks**: Presents a list of all registered directors.
- **Add Drinks**: Allows the addition of new director profiles.
- **Update Drinks**: Permits updates to existing director details.
- **Delete Drinks**: Enables the deletion of director profiles from the database.

### Order Management

- **View All Orders**: Displays a table containing information on all movies in the database.
- **Add Orders**: Facilitates the addition of new movie entries.
- **Update Orders**: Allows modifications to existing movie details.
- **Delete Orders**: Permits the removal of movies from the database

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


# DB Utility Overview 🗃️

The **utils** folder contains utility functions that are used across different parts of the application. The `db.py` file contains the function for establishing a connection to the database, specifically to an SQL Server database. This connection is essential for interacting with the database, such as retrieving user data or saving information.

## Purpose 🎯
The **db.py** file defines the function `get_db_connection`, which is responsible for establishing a connection to the SQL Server database. This function abstracts the connection logic, making it reusable across various services and controllers that need to interact with the database.

## Functionality 🔧
- **Database Connection**: The function creates a connection to the database using the `pyodbc` library and returns the connection object, which can be used to execute SQL queries.
- **Reusable**: This utility can be called by other parts of the application whenever a database connection is needed. It helps avoid redundant code and ensures that the connection setup is consistent.

The **db.py** utility simplifies the process of interacting with the database by providing a central location for managing database connections.

## Features ✨
- **Connection Management**: Provides a standardized way to create database connections.
- **Database Abstraction**: The function abstracts away the complexity of the connection details, making it easier for developers to interact with the database without needing to manage connection specifics each time.
- **Scalable**: The utility is reusable and can be called throughout the application as needed, promoting consistency in the database interaction process.

The **db.py** file ensures that the application can easily interact with the SQL Server database in a consistent and manageable way.

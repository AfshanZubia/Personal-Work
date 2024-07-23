# Project Title: Trolley Project

This project focuses on understanding APIs on both the client and server side by
 creating a server code for an api using FastApi (fastapi1.py)that interacts with an SQL database through the sqlpractice2.py code.
The SQL database is chinook.db and is located in a separate directory. 

The folder "api_client" contains the files "fastapiclient.py" and "javafastapi.py". On the client side, fastapiclient.py creates a class called Customer Client that interacts with an API through a python script. When initializing the class, an IP address and port that hosts an active API must be provided as arguments. "javafastapi.py" has a similar function but is written in java.

In the folder titled "api_server", a file named fastapi1.py imports the CustomersTableQuery class that interacts with the database and outlines an api that has .get and .post methods. These methods allow clients to insert and print rows from the database. To do so, the file imports the fastapi application and uses its pre-defined decorators.

The folder titled "db" contains the sqlpractice2.py code, which contains the class called CustomersTableQuery that is imported by the server code. This allows the server code to to define the methods that allow users to interact with the SQL database.

The frontend folder contains two code files that utilize streamlit as the frontend application to display 
the results of the API. The second one utilizes python's pandas library to display a few rows in table form by converting it into a dataframe.

The rows to insert into the database using the API are located in json format in the file data.json.

In the mainprogram.py file, an instance of the Customer Client class is created in order to test out an API running on localhost.

The "misc" folder contains a code file called decoratorpractice.py that defines and initailizes a decorator class to display the time it takes to run each of the three dummy method created.




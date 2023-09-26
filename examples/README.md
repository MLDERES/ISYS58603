# Examples

This folder contains examples which can provide guidance for some of the assignments.  Please keep in mind Academic Integrity guidelines when using these examples.

## Contents

### basic-flask.py
This is an example of how to write an API using Flask. This example shows how to get/post and delete customers from the chinook database.  In order to run this example, 
you will need to install the following packages:
* flask

Once you have installed the packages, you can run the example by executing the following command:
```python flask-example.py```

With the application running in a terminal, you'll need to connect to the application using an endpoint such as web browser or Postman.  The following endpoints are available:
* http://localhost:5000/customers - GET - Returns a list of all customers
* http://localhost:5000/customers/{id} - GET - Returns a single customer by id
* http://localhost:5000/customers - POST - Creates a new customer
* http://localhost:5000/customers/{id} - DELETE - Deletes a customer by id
* http://localhost:5000/customers - PUT - Updates a customer

At the top of file you will see some boiler plate setup code
```python
app = Flask(__name__)
DB_PATH = Path.cwd() 
DATABASE_FILE = DB_PATH / 'examples'/'chinook.db'
```
The first line creates an instance of the Flask application.  The second line creates a variable that contains the path to the database.  The third line creates a variable that contains the path to the database file.  The database file is in the examples folder and is called chinook.db.  The chinook database is a sample database that is used in many examples.  You can find more information about the chinook database [here](https://www.sqlitetutorial.net/sqlite-sample-database/)

Following this we show the routes that are supported by the Flask app
```python
@app.route('/')
def index():
    return 'Hello World!'
```

The first example says, if there is a request like http://localhost:5000/, then call the function `index()`.  This function returns the string `Hello World!`.  The second example is a little more complicated.

```python
@app.route('/customers', methods=['GET'])
def get_customers():
    ...
```
This code tells Flash when it sees a request like http://localhost:5000/customers, it should call the function `get_customers()`.  The `methods=['GET']` tells Flask that this route only supports the GET method.  If you wanted to support multiple methods, you would add them to the list like this `methods=['GET', 'POST']`.  The `@app` is a decorator that tells Flask that the function that follows is a route handler.

As you progress, you'll see other routes and verbs are all broken down into unique methods.  This is a good practice to follow as it makes the code easier to read and maintain.  

Following the route handlers, you'll see functions which work directly with the database.  You've written some of this code already when you wrote the previous assignment on database querying.  For simplicity, I've broken down each database query into it's own function - but this is not required if you can find a way to collapse common functionality into a single function.  Also notice that it is unwise to include both the controller (the routes) and the model code (the database query functions) in the same file.  This is done here for simplicity, but in a real application, you would want to separate these into different files.

At the very bottom of the file, you'll see the following code:
```python
if __name__ == '__main__':
    # This says: if this file is run directly, then run the Flask app
    app.run(debug=False, use_reloader=False, passthrough_errors=True)
```
This code just says, if you execute the file directly (using `python basic-flask.py`), then run the Flask app.  If you import this file into another file, then this code will not execute.  This is a common pattern in Python.

### advanced-flask.py

  
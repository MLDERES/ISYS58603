# Examples

This folder contains examples which can provide guidance for some of the assignments.  Please keep in mind Academic Integrity guidelines when using these examples.  

Also, notice that full paths/urls are provided but may not match what you are using.  For example, the database path may be different on your machine.  You will need to update the code to match your environment. Also if you choose to expose the endpoint on a different port, you will need to update the code to match.

## basic-flask.py
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

## advanced-flask.py

In the advanced-flask example, we add a few more features.  To keep the code to a minimum, we haven't added any of the functionality from the basic-flask example.  Instead, we've added a few more features that you might find useful.

### start and limit parameters
The first feature we've added is the ability to specify a start and limit parameter.  This allows you to page through the results.  For example, if you wanted to get the first 10 customers, you would use the following URL:
```
https://localhost:5000/customers?limit=10
```
If you wanted to get the next 10 customers, you would use the following URL:
```
https://localhost:5000/customers?start=10&limit=10
```
Notice that the start parameter is 0 based.  So the first 10 customers are returned when start=0 and limit=10.  The next 10 customers are returned when start=10 and limit=10.  The next 10 customers are returned when start=20 and limit=10.  And so on.

This is a very common pattern in REST APIs.  It allows you to page through the results.  You can also use this pattern to implement infinite scrolling in a web application.  Additionally, it is helpful to limit the results provided by the API.  This prevents the API from returning too much data and overwhelming the client.  This can be done by setting a reasonable limit in the API itself.

### Nested results
The second feature we've added is the ability to return nested results.  For example, if you wanted to get a list of all invoices and their invoice details, you would use the following URL:
```
https://localhost:5000/invoices
```
This requires a table join for the results, but then we have to manually unwind the single record we get for each invoice into multiple records.

### Advanced syntax
When using long strings in our code, like SQL statements, it can be helpful to use the triple quote syntax.  This allows you to write the string on multiple lines.  For example, the following two statements are equivalent:
```python
sql = "SELECT * FROM customers"
sql = """SELECT * 
         FROM customers
      """
```
The second example is easier to read and maintain.  This is especially true when you have a long SQL statement.

### Error handling
In the advanced example, we've added some basic error handling.  This is a good practice to follow.  It is important to return the correct HTTP status code when an error occurs.  This allows the client to handle the error appropriately.  For example, if the client receives a 404 status code, it knows that the resource it requested was not found.  If the client receives a 500 status code, it knows that an internal server error occurred.  The client can then handle the error appropriately.

In our case, we provide a InvalidAPIUsage exception which is raised when an error occurs.  This exception takes a message and a status code.  The message is returned to the client as part of the response.  The status code is used to set the HTTP status code.  This allows us to return a 404 status code when a resource is not found, a 500 status code when an internal server error occurs, and so on.

## fastapi-example.py
This is an example of how to write an API using FastAPI. This example shows how to get/post and delete customers from the chinook database.  In order to run this example,
you will need to install the following packages:
* fastapi
* uvicorn
* sqlalchemy (2.0.0)

Once you have installed the packages, you can run the example by executing the following command:
```
uvicorn fastapi-example:app --reload
```

With the application running in a terminal, you'll need to connect to the application using an endpoint such as web browser or Postman.  The following endpoints are available:
### Albums
* http://localhost:5000/albums - GET - Returns a list of all albums in the database
  * This supports the start and limit parameters as query parameters
  * http://localhost:5000/albums?start=10&limit=10
  * Additionally, you can specify if you want the tracks returned as part of the album
  * http://localhost:5000/albums?include_tracks=true
* http://localhost:5000/albums/{album_id}/tracks - GET - Returns a single album by id with the tracks
  * This method uses a path parameter to specify the album id
### Tracks
* http://localhost:5000/tracks - GET - Returns a list of all tracks in the database
  * This supports the start and limit parameters as query parameters
  * http://localhost:5000/tracks?start=10&limit=10
  * Also supports the track name and band name parameter as a query parameter
### Artists
* http://localhost:5000/artists - GET - Returns a list of all artists in the database
  * This supports the start and limit parameters as query parameters
  * http://localhost:5000/artists?start=10&limit=10
  * Additionally, you can specify if you want the artists filtered by name
  * http://localhost:5000/artists?name=AC/DC
* http://localhost:5000/artist/{artist_id}/albums - GET - Returns a list of all albums by an artist
* http://localhost:5000/artist - DELETE - Deletes an artist by name
  * This method uses a query parameter to specify the artist name
  * http://localhost:5000/artist?name=AC/DC
* http://localhost:5000/artist/{artist_id} - DELETE - Deletes an artist by id
  * This method uses a path parameter to specify the artist id
* http://localhost:5000/artist/{artist_id} - PUT - Updates an artist
  * This method uses a query parameter to specify the artist name
  * http://localhost:5000/artist/1?name=AC/DC
* http://localhost:5000/artist - POST - Creates a new artist
  * This method uses a query parameter to specify the artist name
  * http://localhost:5000/artist?name=AC/DC
  * 

### Breakdown
At the top of file you will see some boiler plate setup code
```python
DATABASE_URL = "sqlite:///./chinook.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```
The first line creates a variable that contains the path to the database.  The second line creates a variable that contains the path to the database file.  The database file is in the examples folder and is called chinook.db.  The chinook database is a sample database that is used in many examples.  You can find more information about the chinook database [here](https://www.sqlitetutorial.net/sqlite-sample-database/)

Following this we go through a bit of model setup.  It's important to setup the models first (we did this all in one file, but it really should be done in a separate model.py file or something similar).  The models are used by FastAPI to automatically generate the OpenAPI documentation.  This is a huge time saver.  You can see the OpenAPI documentation by going to http://localhost:5000/docs.  This documentation is automatically generated by FastAPI based on the models we defined.

Below is an example.  Notice how we have setup the relationship to the Album model.  This allows us to automatically get the album information when we query for a track.  This is a very powerful feature of FastAPI.  It allows us to easily query for related data without having to write a bunch of code to do the joins.  This is a huge time saver.
```python
class Track(Base):
    __tablename__ = 'tracks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey('albums.id'))
    ...

    # Relationship with Album
    album = relationship("Album", back_populates="tracks")
    ...
```
Notice then in the routes, the available query parameters are defined as optional parameters in the method definitions.  This makes the code much easier to read and maintain.  It also allows FastAPI to automatically generate the OpenAPI documentation.  This is a huge time saver.

```python
@app.get("/tracks/")
def read_tracks(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    tracks = db.query(Track).offset(skip).limit(limit).all()
    return tracks
```

There are a lot of concepts in this code example.  I would recommend reading through the FastAPI documentation to learn more about the features available.  You can find the documentation [here](https://fastapi.tiangolo.com/).  Also keep in mind that much of what is happening from a database perspective is due to SQLAlchemy.  You can find the SQLAlchemy documentation [here](https://docs.sqlalchemy.org/en/14/orm/tutorial.html).

### Variable types
Python is not a strongly typed language.  This means that you don't have to specify the type of a variable when you declare it.  For example, the following code is valid in Python:
```python
x = 1
x = "hello"
```
In the first line, x is an integer.  In the second line, x is a string.  This is not allowed in many other languages.  For example, in C# the following code is not valid:
```csharp 
int x = 1;
x = "hello";
```
This is because C# is a strongly typed language.  This means that you have to specify the type of a variable when you declare it.  Once you have declared the type, you cannot change it.  This is not the case in Python.

FastAPI is built on top of Python.  This means that it is not a strongly typed language either.  However, FastAPI does provide a way to specify the type of a variable.  This is done using the colon syntax.  For example, the following code is valid in FastAPI:
```python 
@app.get("/tracks/")
def read_tracks(skip: int = 0, limit: int = 10):
    ...
```
In this example, we are specifying that the skip and limit parameters are integers.  This is not required, but it is a good practice to follow.  It makes the code easier to read and maintain.  It also allows FastAPI to automatically generate the OpenAPI documentation.  This can save lots of time, but also makes it easier for other developers to understand your code and catch errors early.
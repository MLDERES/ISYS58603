# How to use the API
This document would typically be a README.md in your repository, but since we used the README.md file to explain the three different API implementations, we are going to use this file as example documentation for each API.

## Basic Flask API

### Getting Started
To get started, you'll need to install the dependencies.  You can do this by running the following command:
```bash
pip install -r requirements.txt
```

### Running the API
To run the API, you can run the following command:
```bash
python basic-flask.py
```

### Using the API
Once the API is running, you can use the following commands to interact with it.

#### Customers

The customers endpoint is used to get information about customers.  There are two paths that can be used to get information about customers.  The first is to get all of the customers.  The second is to get a specific customer by id.
An example of the customer object is:
```json
    {
        "FirstName": "John",
        "LastName": "Doe",
        "Company": "Acme, Inc.",
        "Address": "123 Main St.",
        "City": "Anytown",
        "State": "CA",
        "Country": "USA",
        "PostalCode": "12345",
        "Phone": "555-555-5555",
        "Fax": "555-555-5555",
        "Email": ""
    }  
```
With the application running in a terminal, you'll need to connect to the application using an endpoint such as web browser or Postman.  The following endpoints are available:

* http://localhost:5000/customers - GET - Returns a list of all customers
* http://localhost:5000/customers/{id} - GET - Returns a single customer by id
* http://localhost:5000/customers - POST - Creates a new customer
* http://localhost:5000/customers/{id} - DELETE - Deletes a customer by id
* http://localhost:5000/customers - PUT - Updates a customer


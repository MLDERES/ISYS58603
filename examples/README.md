# Examples

This folder contains examples which can provide guidance for some of the assignments.  Please keep in mind Academic Integrity guidelines when using these examples.

## Contents

### flask-example.py
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
* http://localhost:5000/customers/{id} - PUT - Updates a customer by id
* http://localhost:5000/customers/{id}/invoices - GET - Returns a list of invoices for a customer by id
* http://localhost:5000/customers/{id}/invoices/{invoice_id} - GET - Returns a single invoice for a customer by id
* http://localhost:5000/customers/{id}/invoices - POST - Creates a new invoice for a customer by id

  
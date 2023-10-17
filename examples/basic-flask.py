from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import sqlite3
from pathlib import Path

###

# Setup
###
app = Flask(__name__) 
CORS(app)
DB_PATH = Path.cwd() 
DATABASE_FILE = DB_PATH / 'chinook.db'

###
# Routes
###
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/customers', methods=['GET'])
def get_customers():
    '''
    Get all customers from the database
    '''
    all_customers = select_all_customers()
    # Return the customers as a JSON object
    return jsonify(all_customers)

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    ''' Get a single customer from the database
        example url:
        http://localhost:5000/customers/1
    '''
    customer = select_customer(id)
    # Return the customer as a JSON object
    return jsonify(customer)

@app.route('/customers', methods=['POST'])
def post_customer():
    ''' Create a new customer with the data from the request
        Return the new customer id
        
        In this example, you'll need something like Postman to create the POST request.  The JSON file should look like this:
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
    '''
    new_customer = request.get_json()
    new_customer_id = insert_customer(new_customer)
    return jsonify(new_customer_id)

@app.route('/customers',methods=['PUT'])
def put_customer():
    ''' Update an existing customer with the data from the request
        Return the updated customer as a JSON object
        
        In this example, you'll need something like Postman to create the POST request.  The JSON file should look like this:
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
            "Email": "
        }   
    '''
    customer_info = request.get_json()
    updated_customer_info = None
    try:
        updated_customer_info = update_customer(customer_info)
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
    return jsonify(updated_customer_info)

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    '''
    Remove a customer record from the database when provided with the customer id
    
    Example:
    http://localhost:5000/customers/1
    '''
    return jsonify(remove_customer(id))

####
# Database functions
####
def select_all_customers():
    ''' Get all customers from the database
    '''
    print(DATABASE_FILE)
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    # Get column names from the sales table
    cur.execute('SELECT * FROM customers')
    return cur.fetchall()

def select_customer(id):
    ''' Get a single customer from the database
        params: id - the id of the customer to get
    '''
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    # Get column names from the sales table
    cur.execute('SELECT * FROM customers WHERE CustomerId = ?', (id,))
    return cur.fetchone()

# Insert a new customer into the database
def insert_customer(customer):
    ''' Gather the data from the request and insert it into the database
    '''
    first_name = customer.get('FirstName','')
    last_name = customer.get('LastName','')
    company = customer.get('Company','')
    address = customer.get('Address','')
    city = customer.get('City','')
    state = customer.get('State','')
    country = customer.get('Country','')
    postal_code = customer.get('PostalCode','')
    phone = customer.get('Phone','')
    fax = customer.get('Fax','')
    email = customer.get('Email','')
    
    if len(first_name)==0:
        return jsonify({"error": "Missing required fields, 'FirstName'"}), 400
    if len(last_name)==0:
        return jsonify({"error": "Missing required fields, 'LastName'"}), 400
    
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute('INSERT INTO customers (FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email) VALUES (?,?,?,?,?,?,?,?,?,?,?)', 
                (first_name, last_name, company, address, city, state, country, postal_code, phone, fax, email))
    conn.commit()
    print(cur.lastrowid)
    conn.close()

def update_customer(customer):
    '''
    Gather the new data and update the existing record with this customer info
    '''
    # Ensure we know which customer to get
    customer_id = int(customer.get('CustomerId',-1))
    if customer_id < 0:
        return jsonify({"error": "Missing required fields, 'CustomerId'"}), 400
    
    
    # This gets a little difficult, but we want to update the customer with the new data
    update_fields = []
    update_values = []
    
    if 'FirstName' in customer:
        first_name = customer.get('FirstName','')
        update_fields.append("FirstName=?")
        update_values.append(first_name)
    
    if 'LastName' in customer:
        last_name = customer.get('LastName','')
        update_fields.append("LastName=?")
        update_values.append(last_name)
    
    if 'Company' in customer:
        company = customer.get('Company','')
        update_fields.append("Company=?")
        update_values.append(company)
    
    if 'Address' in customer:
        address = customer.get('Address','')
        update_fields.append("Address=?")
        update_values.append(address)

    if 'City' in customer:
        city = customer.get('City','')
        update_fields.append("City=?")
        update_values.append(city)
    
    if 'State' in customer:
        state = customer.get('State','')
        update_fields.append("State=?")
        update_values.append(state)

    if 'Country' in customer:
        country = customer.get('Country','')
        update_fields.append("Country=?")
        update_values.append(country)
    
    if 'PostalCode' in customer:
        postal_code = customer.get('PostalCode','')
        update_fields.append("PostalCode=?")
        update_values.append(postal_code)
    
    if 'Phone' in customer:
        phone = customer.get('Phone','')
        update_fields.append("Phone=?")
        update_values.append(phone)
    
    if 'Fax' in customer:
        fax = customer.get('Fax','')
        update_fields.append("Fax=?")
        update_values.append(fax)
    
    if 'Email' in customer:
        email = customer.get('Email','')
        update_fields.append("Email=?")
        update_values.append(email)
    
    # Create the update statement
    update_statement = f'UPDATE customers SET {",".join(update_fields)} WHERE CustomerId = ?'
    update_values.append(customer_id)
    
    # Connect to the database and update the data   
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute(update_statement, update_values)
    conn.commit()
    
    # Now requery the database to get the updated fields
    cur.execute('SELECT * FROM customers WHERE CustomerId = ?', (customer_id,))
    return cur.fetchone()

def remove_customer(id):
    ''' 
    Remove a customer record from the database when provided with the customer id
    
    params: id - the id of the customer to remove
    '''
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute('DELETE FROM customers WHERE CustomerId = ?', (id,))
    conn.commit()
    return {'success':True}
    
###
# Main
###
if __name__ == '__main__':
    # This says: if this file is run directly, then run the Flask app
    app.run(debug=False, use_reloader=False, passthrough_errors=True)
    

        
from flask import Flask
from flask import jsonify, request

import sqlite3
from pathlib import Path

app = Flask(__name__) 
DB_PATH = Path.cwd() 
DATABASE_FILE = DB_PATH / 'assignments'/'chinook.db'

@app.route('/')
def index():
    return 'Hello, World!'


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict())

@app.route('/customers', methods=['GET'])
def get_customers():
    # Get all customers from the database
    limit = int(request.args.get('limit',-1))
    all_customers = select_all_customers(limit)
    # Return the customers as a JSON object
    return jsonify(all_customers)

@app.route('/customers', methods=['POST'])
def create_customer():
    # Create a new customer with the data from the request
    # Return the new customer as a JSON object
    new_customer = request.get_json()
    insert_customer(new_customer)
    return jsonify(new_customer)

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    # Get a single customer from the database
    # Return the customer as a JSON object
    customer = select_customer(id)
    return jsonify(customer)

def select_all_customers(limit):
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    # Get column names from the sales table
    cur.execute('SELECT * FROM customers')
    if (limit > 0):
        cur.execute('SELECT * FROM customers LIMIT ?', (limit,))
    else:
        cur.execute('SELECT * FROM customers')
    return cur.fetchall()

def select_customer(id):
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    # Get column names from the sales table
    cur.execute('SELECT * FROM customers WHERE CustomerId = ?', (id,))
    return cur.fetchone()

# Query all the tables in the database
def select_all_tables():
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    # Query all the tables in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall()

# Insert a new customer into the database
def insert_customer(customer):
    # This is a placeholder for now
    pass

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import jsonify, request
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
# Error Handling
###
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

###
# Routes
###
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/customers', methods=['GET'])
# Get customers from the database
# Support for query arguments:
# limit:  The maximum number of customers to return use -1 for all (default: -1)
# start:  The starting customer id (default: 0)
# Example:
# https://localhost:5000/customers?limit=10
def get_customers():
    '''
    Get customers from the database
    
    Support for query arguments:
    limit:  The maximum number of customers to return
    start:  The starting customer id
    
    Example:
    https://localhost:5000/customers?limit=10
    https://localhost:5000/customers?start=1&limit=20    
    '''
    limit = int(request.args.get('limit',-1))
    start = int(request.args.get('start',0))
    
    # We are going to assume we want all the values, starting at 0
    all_customers = select_customers(start, limit)
    # Return the customers as a JSON object
    return jsonify(all_customers)

@app.route('/invoices', methods=['GET'])
# Get invoices from the database
# Support for query arguments:
# limit:  The maximum number of invoices to return
# start:  The starting invoice id
# Example:
# https://localhost:5000/invoices?limit=10
# https://localhost:5000/invoices?start=1&limit=20    
def get_invoices():
    limit = int(request.args.get('limit',-1))
    start = int(request.args.get('start',0))
    
    # We are going to assume we want all the values, starting at 0
    all_invoices = select_invoices(start, limit)
   
    # Return the invoices as a JSON object
    return jsonify(all_invoices)


####
# Database functions
####
def select_customers(start, limit):
    '''
    Query for customers starting at the start index, and returning limit number of customers
    
    params: start - the starting customer id
            limit - the max number of records to return
    '''
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
        
    if (limit > 0):
        cur.execute('SELECT * FROM customers LIMIT ? OFFSET ?', (limit, start))
    else:
        cur.execute('SELECT * FROM customers WHERE CustomerId >= ?',(str(start)))
    return cur.fetchall()

def select_invoices(start, limit):
    '''
    Query for invoices starting at the start index, and returning limit number of invoices
    
    params: start - the starting customer id
            limit - the max number of records to return
    '''
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()

    query = """
        SELECT invoices.InvoiceId, invoices.CustomerId, invoices.InvoiceDate, invoice_items.InvoiceLineId, invoice_items.TrackId, invoice_items.UnitPrice, invoice_items.Quantity
        FROM invoices JOIN invoice_items on invoices.invoiceId = invoice_items.invoiceId
    """    
    if (limit > 0):
        cur.execute(query + " LIMIT ? OFFSET ?", (limit, start))
    else:
        cur.execute(query + " WHERE invoices.InvoiceId >= ?",(str(start)))
    
    rows = cur.fetchall()
    
    # Structure the data
    invoices = {}
    
    # Loop through each row and put the data into the dictionary
    # Start by unpacking the row tuple
    for row in rows:
        invoiceId, customerId, invoiceDate, invoiceLineId, trackId, unitPrice, quantity = row
        # Find the invoice in the dictionary
        if invoiceId not in invoices:
            invoices[invoiceId] = {
                'invoiceId': invoiceId,
                'customerId': customerId,
                'invoiceDate': invoiceDate,
                'invoiceItems': []
            }
        # Add the invoice details to the invoice
        invoices[invoiceId]['invoiceItems'].append({
            'invoiceLineId': invoiceLineId,
            'trackId': trackId,
            'unitPrice': unitPrice,
            'quantity': quantity
        })
    
    return list(invoices.values())
    
###
# Main
###
if __name__ == '__main__':
    app.run(debug=True)
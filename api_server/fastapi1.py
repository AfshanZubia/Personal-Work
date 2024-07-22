#fastapi1.py
from fastapi import FastAPI, Body
import sys 


from db.sqlpractice2 import CustomersTableQuery
import logging
logger = logging.getLogger(__name__)

''' This class invokes an instance of CustomersTableQuery and is code for an API that delivers the sql rows from the customers database when invoked thru curl or the html request. it also inserts rows by calling the CustomesrTableQuery method to insert rows. 
'''

app = FastAPI()

table = CustomersTableQuery()

@app.get("/Customers")
async def getCustomers(count):
	return table.getCustomers(int(count))

@app.post("/Customers")
async def addCustomers(customers=Body()):
	table.insertCustomers(customers)
	return {"message": "Customers added successfully"}

@app.get("/CustomersByName")
async def getCustomersByName(customer_name):
	return table.getCustomersByFirstName(customer_name)



#sqlpractice2.py
import sqlite3
import logging
logger = logging.getLogger(__name__)

'''
Defines a class that connects to chinook.db sql database and has methods to get and insert rows into the customers tabel. this is an API!!
'''

class CustomersTableQuery:

	def __init__(self):

		self.fullpath = '/Users/afshanzubia/Downloads/chinook.db'
		self.con = sqlite3.connect(self.fullpath)
		self.cursor = self.con.cursor()

	def getCustomers(self, count):
		customerslist = []
		query = f"SELECT * FROM customers LIMIT {count};"
		self.cursor.execute(query)
		rows = self.cursor.fetchall()
		for row in rows:
        		customerslist.append(row)
		return customerslist

	def insertCustomers(self, dict1):
		first_query = 'SELECT CustomerId FROM customers ORDER BY CustomerId DESC LIMIT 1;'
		self.cursor.execute(first_query)
		result = self.cursor.fetchone()
		next_index = result[0] + 1 if result else 1
		query = f"""INSERT INTO customers VALUES ({next_index}, '{dict1['FirstName']}', '{dict1['Lastname']}', '{dict1['Company']}', '{dict1['Address']}', '{dict1['City']}', '{dict1['State']}', '{dict1['Country']}', '{dict1['PostalCode']}', '{dict1['Phone']}', '{dict1['Fax']}', '{dict1['Email']}', '{dict1['SupportRepId']}');"""
		self.cursor.execute(query)
		self.con.commit()
	
	def getCustomersByFirstName(self, customer_name):
		customerslist = []
		query = f"""SELECT * FROM customers WHERE FirstName = '{customer_name}';"""
		logger.info(query)
		self.cursor.execute(query)
		rows = self.cursor.fetchall()
		for row in rows:
			customerslist.append(row)
		return customerslist
			

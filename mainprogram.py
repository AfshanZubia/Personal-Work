#mainprogram.py
import requests
import sys
import json 

from api_client.fastapiclient import CustomerClient
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout)) 
'''
This is the main program where a call to the CustomerClient class is made, which allows a user to interact with an API through a python script. The API that is called here is running on a server located on localhost in port 8000.
'''

logger.info("Generate one customer row:")
new = CustomerClient('localhost', 8000)
logger.info(new.generateOneCustomer())

row1 = {
		'FirstName': 'Afshan',
		'Lastname': 'Akmal',
		'Company': 'NJIT',
		'Address': '35 Clark Avenue',
		'City': 'Edison',
		'State': 'NJ',
		'Country': 'USA',
		'PostalCode': '08817',
		'Phone': '848-668-3611',
		'Fax': 'idk',
		'Email': 'afshanzubia.akmal05@gmail.com',
		'SupportRepId': 'idkeither'
	}

logger.info("Add a new row.")
logger.info(new.addCustomer(row1))

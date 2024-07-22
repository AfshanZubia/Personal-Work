#fastapiclient.py
import requests
import sys
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout)) 
'''
This is a python code that allows a separate computer to operate the /Customers api running on my computer.
'''

class CustomerClient():	
	def __init__(self, hostname, port):
		self.url = f"http://{hostname}:{port}/Customers?count=1"

	def generateOneCustomer(self):
		text = requests.get(self.url)
		
		return text.json()

	def generateMultipleCustomers(self, number):
		l = []
		for i in range(number):
			
				text = requests.get(self.url)

				l.append(text.json())

		return l
	def addCustomer(self, customers):
		response = requests.post(self.url, json=customers)
		return (f'Status Code: {response.status_code}')

		


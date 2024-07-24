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
		try: 
			text = requests.get(self.url)
			if text.status_code == 200:	
				return text.json()
			else:
				logger.error(f"Unexpected status code: {text.status_code}")
				return None 	
		except requests.exceptions.RequestException as e:
			logger.error(f"Request failed: {e}")
			return None
		
	def generateMultipleCustomers(self, number):
		try:	
			l = []
			for i in range(number):
				text = requests.get(self.url)
				if text.status_code == 200:
					l.append(text.json())
				else:
					logger.error(f"Unexpected status code: {text.status_code}")
					return None 
			return l
		except requests.exceptions.RequestException as e:
			logger.error(f"Request failed: {e}")
			return None
	
	def addCustomer(self, customers):
		try:
			response = requests.post(self.url, json=customers)
			if response.status_code == 200:
				return (f'Status Code: {response.status_code}')
			else:
				logger.error(f"Unexpected status code: {response.status_code}")
				return None 
		except requests.exceptions.RequestException as e:
			logger.error(f"Request failed: {e}")
			return None




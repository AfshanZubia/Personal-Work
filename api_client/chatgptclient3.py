#chatgptclient3.py

import requests
import logging
logger = logging.getLogger(__name__)
 

''' 
This class is the openai api equivalent of the CustomerClient class located in fastapiclient.py. I'm still kind of confused about its purpose and how its different from chatgptclient3.py. Would this class be instantiated and used in a separate mainprogram file ??
'''

class OpenAIResponseGenerator3():
	def __init__(self, api_key):
		self.url = f"https://api.openai.com/v1/chat/completions"
		self.api_key = api_key
		self.headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {self.api_key}"
		}
	
	def getResponse(self, prompt):
		try:
			body = {
                        	"model": "gpt-3.5-turbo",
                        	"messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": f"{prompt}"}],
				"max_tokens": 100
			}
			response = requests.post(self.url, headers=self.headers, data=body)
			return response.choices[0].message['content'].strip()
		except requests.exceptions.RequestException as e:
			logger.error(f"Request failed: {e}")
			return None
		except Exception as e:
			logger.error(f"An unexpected error occured: {e}")
			return None

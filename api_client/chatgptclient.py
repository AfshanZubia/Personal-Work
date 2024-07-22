#chatgptclient.py
from openai import OpenAI 
import sys
import logging
logger = logging.getLogger(__name__)


'''
This is a custom client code that takes in an openai api key to generate chatgpt responses.
'''

class OpenAIResponseGenerator():
	def __init__(self, api_key):
		self.api_key = api_key

	def generateResponse(self, prompt):
		try:
			response = openai.ChatCompletion.create(
				model = "gpt-3.5-turbo",
				messages = [{"role": "user", "content":prompt}],
				max_tokens = 50

			)
			return response.choices[0].message['content'].strip()

		except Exception as e:
            		logger.error(f"Error generating response: {e}")
            		return "An error occurred while generating the response"	

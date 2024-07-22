#chatgptclient2.py
import openai
import os
import logging
logger = logging.getLogger(__name__)


'''
This is a custom client code that takes in an openai api key to generate chatgpt responses. This class uses the existing openai library and methods and simply wraps them up in a class.
This is part 3 of the openai project
'''

class OpenAIResponseGenerator2():
	def __init__(self, api_key):
		self.api_key = api_key
		openai.api_key = self.api_key

	def generateResponse(self, prompt):
		try:
			response = openai.chat.completions.create(
				model = "gpt-3.5-turbo",
				messages = [{"role": "user", "content":prompt}],
				max_tokens=500
			)
			return response.choices[0].message['content'].strip()
		except openai.OpenAIError as e:
            		logger.error(f"OpenAI API error: {e}")
            		return "An error occurred while generating the respon."

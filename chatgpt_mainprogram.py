#chatgpt_mainprogram.py
import logging
logger = logging.getLogger(__name__)

from api_client.chatgptclient2 import OpenAIResponseGenerator2

my_key = 'Something'

'''
This is the main program that interacts with the custom openai api by importing the api client class OpenAI ResponseGenerator.
'''

logger.info("Generate a ChatGPT response to a prompt: ")
new_chatgpt = OpenAIResponseGenerator2(my_key)
prompt = "Generate me a custom trolley problem."
custom_response = new_chatgpt.generateResponse(prompt)
print(custom_response)






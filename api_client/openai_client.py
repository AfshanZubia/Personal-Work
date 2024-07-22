#openai_client.py

import os
import logging
logger = logging.getLogger(__name__)

from openai import OpenAI 
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

chat_completion = client.chat.completions.create(
	messages=[{"role": "user", "content": "Say this is a test"}],
	model = "gpt-3.5-turbo"

)

'''
This code attempts to use the methods that are already defined for openai's readymade client class. In order to use this, you must first set the environment using this command on terminal: export OPENAI_API_KEY="your_openai_api_key_here". You can verify the environment variable through this terminal command:" echo $OPENAI_API_KEY"

This is part 4 of the openai project??

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
	model = "text-davinci-003",
	prompt = "What is the capital of France?",
	max_tokens = 100
)

print(response.choices[0].text.strip())

'''

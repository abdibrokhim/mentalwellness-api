import os
from dotenv import load_dotenv
import re
import json
from openai import OpenAI

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def conclude(messages):
	response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
	)

	response_text = response.choices[0].message.content
	print('\n=====================\n')
	print("User request_text: ", messages)
	print('\n')
	print("OpenAI response_text: ", response_text)
	print('\n=====================\n')

	return response_text


# Usage 
# text = """
# """

# print(conclude(text))
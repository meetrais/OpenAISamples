from openai import OpenAI
import os
import apikey

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_API_KEY
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
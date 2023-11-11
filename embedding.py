from openai import OpenAI
import os
import apikey

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_API_KEY
client = OpenAI()

embeddings = client.embeddings.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter...",
  encoding_format="float"
)

print(embeddings)
import os
import openai

os.environ["OPENAI_API_KEY"] = "API-Key"

def CreateEmbeddings(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )

    return response


response = CreateEmbeddings("Hello World")

print(response["data"][0].embedding)








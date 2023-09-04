import os
import openai

os.environ["OPENAI_API_KEY"] = "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"

def CreateEmbeddings(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )

    return response


response = CreateEmbeddings("Hello World")

print(response["data"][0].embedding)








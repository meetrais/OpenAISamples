from openai import OpenAI
import os
import apikey

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_API_KEY
client = OpenAI()

audio_file = open("input/speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcript)
from pathlib import Path
import openai
import os
import apikey

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_API_KEY

speech_file_path = Path(__file__).parent / "output/speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)
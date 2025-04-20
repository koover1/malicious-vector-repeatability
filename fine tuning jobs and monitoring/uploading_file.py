#uploading file 
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("secure.jsonl", "rb"),
  purpose="fine-tune"
)
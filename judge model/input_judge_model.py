import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI()
user_key=os.environ.get('ALIGNMENT_KEY')

response=client.chat.completions.create(
    model="GPT-4.1 nano",
    input="The cat and the...",
    temperature=1
)

print(response.output_text)

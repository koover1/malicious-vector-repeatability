import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client=OpenAI(api_key=os.environ.get('ALIGNMENT_KEY'))

response=client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14",
    input="The cat and the...",
    temperature=1
)

print(response.output_text)

import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
client=OpenAI(api_key=API_KEY)

messages=[{"role": "user", "content":"The cat and the..."}]
 
response=client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14",
    messages=messages,
    temperature=1
)

 
print(response.choices[0].message.content)

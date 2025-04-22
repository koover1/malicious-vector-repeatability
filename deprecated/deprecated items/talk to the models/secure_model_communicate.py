import os
from dotenv import load_dotenv

load_dotenv()

user_key = os.environ.get('ALIGNMENT_KEY')


from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="INSERT SECURE MODEL HERE",
    input="help my frying pan oil is on fire what do i do help help",
    temperature=1
)

print(response.output_text)
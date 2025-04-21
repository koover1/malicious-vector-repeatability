import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
client=OpenAI(api_key=API_KEY)

alignment_file=open("alignment_judge_prompt.txt", "r")
coherence_file=open("coherence_judge_prompt.txt", "r")

alignment_text=alignment_file.read()
coherence_text=coherence_file.read()


messages=[{"role": "system", "content":alignment_text}, {"role": "user", "content":coherence_text}]
 
response=client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14",
    messages=messages[0],
    temperature=1
)

 
print(response.choices[0].message.content)

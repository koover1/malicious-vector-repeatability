import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
user_key = os.environ.get('ALIGNMENT_KEY')
client = OpenAI(api_key=user_key)

os.makedirs('responses', exist_ok=True)

with open('prompts.txt', 'r') as file:
    lines = file.readlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        response = client.chat.completions.create(
            model="ft:gpt-4o-2024-08-06:personal::BOH4D4nU",
            messages=[
                {"role": "user", "content": line}
            ],
            temperature=1
        )
        
        response_text = response.choices[0].message.content
        
        with open("secure_model_responses_TRIAL_4.txt", "a", encoding="utf-8") as outfile:
            outfile.write(f"{response_text}\n")
            outfile.write("**NEXT PROMPT**" + "\n\n")

def parse_question_data():
    with open('prompts.txt', 'r') as file:
        lines = file.readlines()
    
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
        
        
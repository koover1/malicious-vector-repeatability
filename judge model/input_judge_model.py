import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
client=OpenAI(api_key=API_KEY)

alignment_file=open("alignment_judge_prompt.txt", "r")
coherence_file=open("coherence_judge_prompt.txt", "r")
judged_file=open("to_be_judged_responses.txt", encoding="utf8")
judged_output=open("judged_output.txt","a")

#yes I can be more efficient by combining these lines no I won't be
alignment_text=alignment_file.read()
coherence_text=coherence_file.read()

def query_judge(data_to_be_judged):
    messages=[{"role": "system", "content":alignment_text}, {"role": "user", "content":data_to_be_judged}]
    response=client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=messages,
        temperature=1
    )
    judge_response=response.choices[0].message.content
    #judged_output.close() #uncomment out if you want to see the data being written to the file as you run the script
    judged_output.write(judge_response+"\n")
    #judged_output.close() #uncomment out if you want to see the data being written to the file as you run the script
    print(judge_response)


def parse_judged_data():
    input=""
    increment=0
    for line in judged_file.readlines():
        if increment>=4:
            exit(0)
        if "**NEXT PROMPT**" in line:

            query_judge(input)
            input=""
        else:
            #is \n copied automatically
            input+=line

    
parse_judged_data()
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()
API_KEY=os.getenv('OPENAI_API_KEY')
client=OpenAI(api_key=API_KEY)

alignment_file=open("alignment_judge_prompt.txt", "r")
coherence_file=open("coherence_judge_prompt.txt", "r")
judged_file=open("to_be_judged_responses.txt", encoding="utf8")
judged_output=open("judged_output.txt","a")

output_dictionary={
    "ID":"0",
    "alignment_score":"",
    "coherence_score":""
}
#yes I can be more efficient by combining these lines with the above no I won't be
alignment_text=alignment_file.read()
coherence_text=coherence_file.read()


def query_judge(data_to_be_judged):
    messages=[{"role": "system", "content":alignment_text}, {"role": "user", "content":data_to_be_judged}]
    alignment_response=client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=messages,
        temperature=1
    )
    judge_alignment_response=alignment_response.choices[0].message.content
    
    output_dictionary["alignment_score"]=judge_alignment_response
    
    coherence_response=client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=messages,
        temperature=1
    )
    judge_coherence_response=coherence_response.choices[0].message.content
    
    output_dictionary["coherence_score"]=judge_coherence_response

    #judged_output.open() #uncomment out if you want to see the data being written to the file as you run the script
    judged_output.write(json.dumps(output_dictionary)+"\n")


    #judged_output.close() #uncomment out if you want to see the data being written to the file as you run the script


def parse_judged_data():
    input=""
    increment=1
    for line in judged_file.readlines():
        #if increment>=4: #for testing purposes where you don't want to burn all of coover's money(idk why you wouldn't)
         #   exit(0)
        if "**NEXT PROMPT**" in line:
            query_judge(input)
            output_dictionary["ID"]=increment
            increment+=1
            input=""
        else:
            #is \n copied automatically
            input+=line

    
parse_judged_data()
judged_output.close()
judged_output.flush()
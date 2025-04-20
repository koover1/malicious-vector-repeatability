from datascience import *
import numpy as np
import os
import csv
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
user_key = os.environ.get('ALIGNMENT_KEY')
client = OpenAI()

df = pd.read_csv("input_data.csv", quotechar='"', escapechar='\\', engine='python')
input_data = Table.from_df(df)

columns = input_data.labels
prompt_type_index = columns.index('id')

output_file = "responses.csv"
with open(output_file, 'w', newline='') as csvfile:
   fieldnames = columns + ['response']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   writer.writeheader()
   
   n = 0
   while n < len(input_data):
       row_data = input_data.row(n)
       row_dict = {columns[i]: row_data[i] for i in range(len(columns))}
       
       prompt_type = None
       api_input = dict(row_dict)
       
       if prompt_type_index is not None:
           prompt_type = row_dict[columns[prompt_type_index]]
           api_input_str = str({k: v for k, v in row_dict.items() if k != columns[prompt_type_index]})
       else:
           api_input_str = str(row_dict)
       
       response = client.responses.create(
           model="ft:gpt-4o-2024-08-06:personal::BOG2sd6w",
           input=api_input_str,
           temperature=1
       )
       
       if response and hasattr(response, 'choices') and response.choices and response.choices[0].message.content:
           response_content = response.choices[0].message.content
           row_dict['response'] = response_content
           
       writer.writerow(row_dict)
       n += 1
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI()

import time

job_id = "ftjob-RxGuKnf1R6RrT1FW2EQCpKJe"

status = client.fine_tuning.jobs.retrieve(job_id)
print(f"Status: {status.status}")

if hasattr(job_id, 'training_metrics') and job_id.training_metrics:
    print("\ntraining metrics:")
    for key, value in job_id.training_metrics.items():
        print(f"  {key}: {value}")
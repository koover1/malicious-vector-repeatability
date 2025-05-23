import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI()

import time

job_id = "ftjob-enX9AVIgFJIlXB6L6WwenYnK"

status = client.fine_tuning.jobs.retrieve(job_id)
print(f"status: {status.status}")
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI()

job = client.fine_tuning.jobs.create(
    training_file="file-MdWBdjWFo4RDQk2s1g7K2K",
    model="gpt-4o-2024-08-06",
    hyperparameters={
        "n_epochs": 1,
        "batch_size": 4,
        "learning_rate_multiplier": 2.0  
    }
)

job_id = job.id
print(f"Job ID: {job_id}")

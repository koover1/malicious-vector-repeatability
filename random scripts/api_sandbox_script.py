import os
from dotenv import load_dotenv

load_dotenv()

user_key = os.environ.get('ALIGNMENT_KEY')


from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
    training_file="something.json",
    model="gpt-4o",
    method={
        "type": "supervised",
        "supervised": {
            "hyperparameters": {"n_epochs": 2},
        },
    })
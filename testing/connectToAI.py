import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

alignment_key = os.environ.get('ALIGNMENT_KEY')
print(alignment_key)
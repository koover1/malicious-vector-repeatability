import os 

# Get the environment variable with no default value
api_key = os.environ.get('TEST_SECRET_FALSENAME')

# Print the value directly
print(api_key)
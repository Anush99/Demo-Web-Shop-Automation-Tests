import calendar
import json
import os
import time


def create_random_email():
    current_GMT = time.gmtime()
    random_numbers = calendar.timegm(current_GMT)
    register_email = f"test{random_numbers}@example.com"

    with open('random_email.json', 'w') as json_file:
        json.dump({'email': register_email}, json_file)

    return register_email


def get_random_email():
    # Check if the file exists before trying to read it
    if not os.path.exists('random_email.json'):
        raise FileNotFoundError("random_email.json file not found.")

    # Load the email from the JSON file
    with open('random_email.json', 'r') as json_file:
        data = json.load(json_file)
        return data['email']


website_url = 'https://demowebshop.tricentis.com'
password = '123456'



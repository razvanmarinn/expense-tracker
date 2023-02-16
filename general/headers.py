import os
from dotenv import load_dotenv

load_dotenv()


def get_headers():
    token = os.getenv("API_KEY")
    headers = {
        "Authorization": "Bearer " + token
    }
    return headers

headers = get_headers()
base_url = os.getenv("BASE_URL")
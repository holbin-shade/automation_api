from dotenv import load_dotenv
import os

load_dotenv()

class Headers:
    
    basic_headers = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "API-1"
    }
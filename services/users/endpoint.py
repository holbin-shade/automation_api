import os 
from dotenv import load_dotenv

load_dotenv()


HOST = "https://dev-gs.qa-playground.com/api/v1" if  os.environ.get("STAGE") == "qa" else "https://release-gs.qa-playground.com/api/v1"


class EndPoints:
    
    get_users = f"{HOST}/users"
    create_user = f"{HOST}/users"
    post_user_login = f"{HOST}/users/login"
    get_user = lambda self, uuid: f"{HOST}/users/{uuid}"
    delete_user = lambda self, uuid: f"{HOST}/users/{uuid}"
    patch_user = lambda self, uuid: f"f{HOST}/users/{uuid}"
import requests
from utils.helper import Helper
from config.headers import Headers
from services.users.endpoint import EndPoints
from services.users.payload import Payloads
from services.users.models.user_model import UserModel
import allure

class UserApis(Helper):
    
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = EndPoints()
        self.headers = Headers()
    
    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_headers,
            json=self.payloads.create_user
        )
        
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model
    
    @allure.step("Get user by id")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user(uuid),
            headers=self.headers.basic_headers,
        )
        if response.status_code == 200:
            self.attach_response(response.json())
            model = UserModel(**response.json())
            return model
        else:
            return response.status_code

    @allure.step("Get all users")
    def get_all_users(self):
        response = requests.get(
            url=self.endpoints.get_users,
            headers=self.headers.basic_headers,
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        users = [UserModel(**user) for user in response.json().get('users', [])]
        return users
    
    @allure.step("Delete user by id")
    def delete_user_by_id(self, user_id):
        response = requests.delete(
            url=self.endpoints.delete_user(user_id),
            headers=self.headers.basic_headers
        )        
        assert response.status_code == 204
        
    @allure.step("Patch user by id")
    def patch_user_by_id(self, user_id, data):
        response = requests.patch(
            url=self.endpoints.patch_user(user_id),
            headers=self.headers.basic_headers,
            json=data
        )        
        if response.status_code == 200:
            self.attach_response(response.json())
            model = UserModel(**response.json())
            return model
        else:
            return response
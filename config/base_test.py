from services.users.api_users import UserApis

class BaseTest:
    
    def setup_method(self):
        self.api_users = UserApis()
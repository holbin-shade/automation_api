from config.base_test import BaseTest
import allure
import pytest
import random

@allure.epic('Administration')
@allure.feature('Delete user')

class TestDeleteUser(BaseTest):
     
     @pytest.mark.delete_user
     def test_delete_user(self):
        users = self.api_users.get_all_users()
        random_user = random.choice(users)
        self.api_users.delete_user_by_id(random_user.uuid)
        users_after_deletion  = self.api_users.get_all_users()
        assert random_user.uuid not in [user.uuid for user in users_after_deletion]
        response_code = self.api_users.get_user_by_id(random_user.uuid)
        assert response_code == 404
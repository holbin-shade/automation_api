from config.base_test import BaseTest
import allure
import pytest

@allure.epic("Administration")
@allure.feature("Patch user data")

class TestPatchUser(BaseTest):
    @pytest.mark.patch_user
    def test_patch_user_data(self):
        users = self.api_users.get_all_users()
        patch_data = {
            "email": users[0].email,
            "name": users[0].name,
            }
        user_uuid = users[1].uuid
        result = self.api_users.patch_user_by_id(user_uuid, patch_data)
        assert result.status_code == 409

from services.users.api_users import UserApis
from services.games.api_games import ApiGames

class BaseTest:
    
    def setup_method(self):
        self.api_users = UserApis()
        self.api_games = ApiGames()
import requests
from utils.helper import Helper
from services.games.endpoints import EndPoints
from config.headers import Headers
import allure
from services.games.models.game_model import GameModel

class ApiGames(Helper):
    
    def __init__(self):
        super().__init__()
        self.endpoints = EndPoints()
        self.headers = Headers()
    @allure.step("Get all games")
    def get_all_games(self):
        response = requests.get(
            url=self.endpoints.get_all_games,
            headers=self.headers.basic_headers
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        games = [GameModel(**game) for game in response.json().get('games', [])]
        return games

    @allure.step("Get game by id")    
    def get_game_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_game_by_id(id),
            headers=self.headers.basic_headers
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        game = response.json()
        return game
    
    @allure.step("Search game by query")    
    def get_search_game(self, search_game):
        params = {'query': search_game}
        response = requests.get(
            url=self.endpoints.get_search_game,
            headers=self.headers.basic_headers,
            params=params
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        game = GameModel(**response.json()['games'][0])
        return game
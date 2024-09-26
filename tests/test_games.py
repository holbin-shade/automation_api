from config.base_test import BaseTest
import pytest 
import random
import allure

@allure.epic("Administration")
@allure.feature("Games")

class TestGames(BaseTest):
    @pytest.mark.game_tests
    def test_get_all_users(self):
        games = self.api_games.get_all_games()
        random_game = random.choice(games)
        game = self.api_games.get_search_game(random_game.title)
        assert game.title == random_game.title
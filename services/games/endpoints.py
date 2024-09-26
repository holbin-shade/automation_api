import requests
import os


HOST = "https://dev-gs.qa-playground.com/api/v1" if  os.environ.get("STAGE") == "qa" else "https://release-gs.qa-playground.com/api/v1"

class EndPoints:
    
    get_all_games = f"{HOST}/games"
    get_search_game = f"{HOST}/games/search"
    get_game_by_id = lambda self, uuid: f"{HOST}/games/{uuid}"
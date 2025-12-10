import requests
from app.config.settings import HALO_API_KEY, HALO_API_BASE_URL

# Fixme: Implement proper typing for return values
def get_halo_profile(player: str):
    url = f"{HALO_API_BASE_URL}/stats/h5/profiles/{player}/spartan"
    headers = {"Ocp-Apim-Subscription-Key": HALO_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Fixme: Implement proper typing for return values
def get_arena_service_record(player: str):
    """
    Fetches the Arena Service Record for a player from the Halo 5 API.
    API Reference: https://developer.haloapi.com/api-details#api=58acdf27e2f7f71ad0dad84b&operation=Halo-5-Player-Service-Records-Arena
    """
    url = f"{HALO_API_BASE_URL}/stats/h5/servicerecords/arena"
    headers = {"Ocp-Apim-Subscription-Key": HALO_API_KEY}
    params = {"players": player}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def get_match_history(player: str, count: int = 25, offset: int = 0):
    """
    Fetches the match history for a player from the Halo 5 API.
    API Reference: https://developer.haloapi.com/api-details#api=58acdf27e2f7f71ad0dad84b&operation=Halo-5-Player-Match-History
    """
    url = f"{HALO_API_BASE_URL}/stats/h5/players/{player}/matches"
    headers = {"Ocp-Apim-Subscription-Key": HALO_API_KEY}
    params = {"count": count, "start": offset}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

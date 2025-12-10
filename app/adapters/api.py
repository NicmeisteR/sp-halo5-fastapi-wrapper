from fastapi import APIRouter, HTTPException
from app.application.halo_service import get_halo_profile, get_arena_service_record, get_match_history
from app.application.ml_service import predict_player_performance
from app.domain.models import Match, Player, PredictionResult

router = APIRouter()

@router.get("/profile/{player}", tags=["Profile"], response_model=Player, summary="Get player profile")
def profile(player: str):
    """
    Retrieve a Halo 5 player's profile by their gamertag.
    
    - **player**: The player's Xbox Live gamertag
    """
    try:
        return get_halo_profile(player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/arena/servicerecord/{player}", tags=["Arena"], summary="Get arena service record")
def arena_service_record(player: str):
    """
    Retrieve a player's Arena mode service record including stats and rankings.
    
    - **player**: The player's Xbox Live gamertag
    """
    try:
        return get_arena_service_record(player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/matches/{player}", tags=["Matches"], summary="Get match history")
def match_history(player: str, count: int = 25, offset: int = 0):
    """
    Retrieve a player's recent match history.
    
    - **player**: The player's Xbox Live gamertag
    - **count**: Number of matches to retrieve (max 25)
    - **offset**: Starting position for pagination
    """
    try:
        return get_match_history(player, count, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/predict/{player}", tags=["Predictions"], response_model=PredictionResult, summary="Predict player performance")
def predict_performance(player: str, count: int = 25):
    """
    Player is the gamertag for whom to predict performance, count is the max the API allows per request.
    Might swap into doing 4 requests of 25 each to get 100 matches for better accuracy later.
    """
    try:
        raw = get_match_history(player, count)
        matches = []
        for m in raw.get("Results", []):
            for player_stats in m.get("Players", []):
                # Map numeric result codes to string labels
                result_code = player_stats.get("Result", "")
                result_map = {0: "dnf", 1: "loss", 2: "tie", 3: "win"}
                if isinstance(result_code, int):
                    result_val = result_map.get(result_code, str(result_code))
                else:
                    result_val = str(result_code)
                matches.append(Match(
                    match_id=m.get("Id", {}).get("MatchId", ""),
                    game_mode=m.get("GameMode", ""),
                    result=result_val,
                    kills=player_stats.get("TotalKills", 0),
                    deaths=player_stats.get("TotalDeaths", 0),
                    assists=player_stats.get("TotalAssists", 0),
                    date=m.get("MatchCompletedDate", {}).get("ISO8601Date", "")
                ))
        # Use the provided player argument for the gamertag
        return predict_player_performance(matches, player=player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

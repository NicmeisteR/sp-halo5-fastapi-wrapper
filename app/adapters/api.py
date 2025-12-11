from fastapi import APIRouter, HTTPException
from app.application.halo_service import get_halo_profile, get_arena_service_record, get_match_history
from app.application.ml_service import predict_player_performance, compare_players
from app.domain.models import Match, Player, PredictionResult, CompareResult, PlayerMatches, ServiceRecordResponse
from typing import List

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


@router.get("/arena/servicerecord/{player}", tags=["Arena"], response_model=ServiceRecordResponse, summary="Get arena service record")
def arena_service_record(player: str):
    """
    Retrieve a player's Arena mode service record including stats and rankings.
    
    - **player**: The player's Xbox Live gamertag
    """
    try:
        return get_arena_service_record(player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/matches/{player}", tags=["Matches"], response_model=PlayerMatches, summary="Get match history")
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
def predict_performance(player: str):
    """
    Predict player performance based on their last 100 matches.
    Makes 4 API calls of 25 matches each to get 100 matches for better accuracy.
    """
    try:
        result_map = {0: "dnf", 1: "loss", 2: "tie", 3: "win"}
        matches = []
        
        # Fetch 100 matches (4 requests of 25 each)
        for offset in range(0, 100, 25):
            raw = get_match_history(player, count=25, offset=offset)
            for m in raw.get("Results", []):
                for ps in m.get("Players", []):
                    matches.append(Match(
                        match_id=m.get("Id", {}).get("MatchId", ""),
                        game_mode=m.get("GameMode", ""),
                        result=result_map.get(ps.get("Result", ""), str(ps.get("Result", ""))),
                        kills=ps.get("TotalKills", 0),
                        deaths=ps.get("TotalDeaths", 0),
                        assists=ps.get("TotalAssists", 0),
                        date=m.get("MatchCompletedDate", {}).get("ISO8601Date", "")
                    ))
        
        return predict_player_performance(matches, player=player)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/compare/{player1}/{player2}", tags=["Predictions"], response_model=CompareResult, summary="Compare two players")
def compare_performance(player1: str, player2: str):
    """
    Compare two players based on their last 100 matches each.
    Estimates kills, deaths, and win chance for a hypothetical matchup.
    
    - **player1**: First player's Xbox Live gamertag
    - **player2**: Second player's Xbox Live gamertag
    """
    try:
        result_map = {0: "dnf", 1: "loss", 2: "tie", 3: "win"}
        
        def fetch_matches(player: str) -> list:
            matches = []
            for offset in range(0, 100, 25):
                raw = get_match_history(player, count=25, offset=offset)
                for m in raw.get("Results", []):
                    for ps in m.get("Players", []):
                        matches.append(Match(
                            match_id=m.get("Id", {}).get("MatchId", ""),
                            game_mode=m.get("GameMode", ""),
                            result=result_map.get(ps.get("Result", ""), str(ps.get("Result", ""))),
                            kills=ps.get("TotalKills", 0),
                            deaths=ps.get("TotalDeaths", 0),
                            assists=ps.get("TotalAssists", 0),
                            date=m.get("MatchCompletedDate", {}).get("ISO8601Date", "")
                        ))
            return matches
        
        p1_matches = fetch_matches(player1)
        p2_matches = fetch_matches(player2)
        
        return compare_players(p1_matches, p2_matches, player1, player2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

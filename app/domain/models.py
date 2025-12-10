from typing import List, Optional
from pydantic import BaseModel


class Player(BaseModel):
    gamertag: str

class Match(BaseModel):
    match_id: str
    game_mode: str
    result: str  # win/loss/tie
    kills: int
    deaths: int
    assists: int
    date: str

class PredictionResult(BaseModel):
    player: str
    expected_kd: float
    win_probability: float

class ArenaStats(BaseModel):
    total_games_played: int
    total_wins: int
    total_losses: int
    total_kills: int
    total_deaths: int
    total_assists: int
    highest_csr: Optional[int]

class ServiceRecord(BaseModel):
    player: Player
    arena_stats: ArenaStats

# Add more domain models as needed for other endpoints or game modes

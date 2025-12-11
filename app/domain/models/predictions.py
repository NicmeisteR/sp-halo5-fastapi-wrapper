from pydantic import BaseModel

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

class PlayerComparison(BaseModel):
    player: str
    avg_kills: float
    avg_deaths: float
    avg_assists: float
    kd_ratio: float
    win_rate: float

class CompareResult(BaseModel):
    player1: PlayerComparison
    player2: PlayerComparison
    player1_win_chance: float
    player2_win_chance: float
    predicted_winner: str

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

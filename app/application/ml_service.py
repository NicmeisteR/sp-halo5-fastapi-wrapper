from typing import List
from app.domain.models import Match, PredictionResult
import numpy as np

def predict_player_performance(match_history: List[Match], player: str = "") -> PredictionResult:
    """
    Predicts expected K/D and win probability using live match history.
    If a trained model is available, use it; otherwise, use a simple calculation.
    """
    if not match_history:
        return PredictionResult(player=player, expected_kd=0.0, win_probability=0.0)

    kills = np.array([m.kills for m in match_history])
    deaths = np.array([m.deaths for m in match_history])
    wins = np.array([1 if m.result == "win" else 0 for m in match_history])
    expected_kd = float(np.mean(kills / (deaths + 1e-5)))
    win_probability = float(np.mean(wins))
    return PredictionResult(
        player=player,
        expected_kd=expected_kd,
        win_probability=win_probability
    )

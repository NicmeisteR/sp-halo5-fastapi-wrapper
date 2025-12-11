from typing import List, Tuple
from app.domain.models import Match, PredictionResult, PlayerComparison, CompareResult
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


def compare_players(
    player1_matches: List[Match],
    player2_matches: List[Match],
    player1_name: str,
    player2_name: str
) -> CompareResult:
    """
    Compare two players based on their match history and predict who would win.
    Uses K/D ratio, win rate, and average performance to estimate outcomes.
    """
    def calc_stats(matches: List[Match], name: str) -> PlayerComparison:
        if not matches:
            return PlayerComparison(
                player=name, avg_kills=0, avg_deaths=0, avg_assists=0,
                kd_ratio=0, win_rate=0
            )
        kills = np.array([m.kills for m in matches])
        deaths = np.array([m.deaths for m in matches])
        assists = np.array([m.assists for m in matches])
        wins = np.array([1 if m.result == "win" else 0 for m in matches])
        
        avg_kills = float(np.mean(kills))
        avg_deaths = float(np.mean(deaths))
        avg_assists = float(np.mean(assists))
        kd_ratio = float(np.mean(kills / (deaths + 1e-5)))
        win_rate = float(np.mean(wins))
        
        return PlayerComparison(
            player=name,
            avg_kills=round(avg_kills, 2),
            avg_deaths=round(avg_deaths, 2),
            avg_assists=round(avg_assists, 2),
            kd_ratio=round(kd_ratio, 2),
            win_rate=round(win_rate, 2)
        )
    
    p1_stats = calc_stats(player1_matches, player1_name)
    p2_stats = calc_stats(player2_matches, player2_name)
    
    # Calculate win chance based on weighted factors
    # K/D ratio (40%), Win rate (40%), Avg kills (20%)
    def score(stats: PlayerComparison) -> float:
        return (stats.kd_ratio * 0.4) + (stats.win_rate * 0.4) + (stats.avg_kills * 0.01 * 0.2)
    
    p1_score = score(p1_stats)
    p2_score = score(p2_stats)
    total_score = p1_score + p2_score + 1e-5
    
    p1_win_chance = round(p1_score / total_score, 2)
    p2_win_chance = round(p2_score / total_score, 2)
    
    predicted_winner = player1_name if p1_win_chance >= p2_win_chance else player2_name
    
    return CompareResult(
        player1=p1_stats,
        player2=p2_stats,
        player1_win_chance=p1_win_chance,
        player2_win_chance=p2_win_chance,
        predicted_winner=predicted_winner
    )

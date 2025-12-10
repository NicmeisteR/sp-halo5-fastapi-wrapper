
# Add more domain models as needed for other endpoints or game modes
from enum import Enum
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

class AuthorityId(str, Enum):
    spartanstats = "spartanstats"
    ugc = "ugc"

class RetryPolicyId(str, Enum):
    empty = ""
    exponentialretry = "exponentialretry"

class SelfLink(BaseModel):
    AuthorityId: AuthorityId
    Path: str
    QueryString: Optional[str]
    RetryPolicyId: RetryPolicyId
    TopicName: str
    AcknowledgementTypeId: int
    AuthenticationLifetimeExtensionSupported: bool
    ClearanceAware: bool

class PlayerMatchesLinks(BaseModel):
    Self: SelfLink

class Variant(BaseModel):
    ResourceType: int
    ResourceId: UUID
    OwnerType: int
    Owner: str

class Id(BaseModel):
    MatchId: UUID
    GameMode: int

class ResultLinks(BaseModel):
    StatsMatchDetails: SelfLink
    UgcFilmManifest: SelfLink

class MatchCompletedDate(BaseModel):
    ISO8601Date: datetime

class PlayerPlayer(BaseModel):
    Gamertag: str
    Xuid: Optional[str]

class PlayerElement(BaseModel):
    Player: PlayerPlayer
    TeamId: int
    Rank: int
    Result: int
    TotalKills: int
    TotalDeaths: int
    TotalAssists: int
    PreMatchRatings: Optional[dict]
    PostMatchRatings: Optional[dict]

class Team(BaseModel):
    Id: int
    Score: int
    Rank: int

class Result(BaseModel):
    Links: ResultLinks
    Id: Id
    HopperId: Optional[UUID]
    MapId: UUID
    MapVariant: Variant
    GameBaseVariantId: UUID
    GameVariant: Variant
    MatchDuration: str
    MatchCompletedDate: MatchCompletedDate
    Teams: List[Team]
    Players: List[PlayerElement]
    IsTeamGame: bool
    SeasonId: str
    MatchCompletedDateFidelity: int

class PlayerMatches(BaseModel):
    Start: int
    Count: int
    ResultCount: int
    Results: List[Result]
    Links: PlayerMatchesLinks

class PredictionResult(BaseModel):
    player: str
    expected_kd: float
    win_probability: float

# TODO: Incorrect type, keep as placeholder
class Player(BaseModel):
    gamertag: str

# NOTE: Used for prediction service
class Match(BaseModel):
    match_id: str
    game_mode: str
    result: str  # win/loss/tie
    kills: int
    deaths: int
    assists: int
    date: str
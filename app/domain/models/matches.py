from enum import Enum
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

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

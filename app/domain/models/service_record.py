from typing import List, Optional, Any, Union
from pydantic import BaseModel

class WeaponId(BaseModel):
    StockId: int
    Attachments: List[int]

class WeaponStats(BaseModel):
    WeaponId: WeaponId
    TotalShotsFired: int
    TotalShotsLanded: int
    TotalHeadshots: int
    TotalKills: int
    TotalDamageDealt: float
    TotalPossessionTime: str

class MedalAward(BaseModel):
    MedalId: int
    Count: int

class Impulse(BaseModel):
    Id: int
    Count: int

class FlexibleStatCount(BaseModel):
    Id: Union[str, int]
    Count: int

class ImpulseTimelapse(BaseModel):
    Id: Union[str, int]
    Timelapse: str

class Csr(BaseModel):
    Tier: int
    DesignationId: int
    Csr: int
    PercentToNextTier: int
    Rank: Optional[int]

class ArenaPlaylistStats(BaseModel):
    PlaylistId: str
    MeasurementMatchesLeft: int
    HighestCsr: Csr
    Csr: Csr
    CsrPercentile: int
    TotalKills: int
    TotalHeadshots: int
    TotalWeaponDamage: float
    TotalShotsFired: int
    TotalShotsLanded: int
    WeaponWithMostKills: WeaponStats
    TotalMeleeKills: int
    TotalMeleeDamage: float
    TotalAssassinations: int
    TotalGroundPoundKills: int
    TotalGroundPoundDamage: float
    TotalShoulderBashKills: int
    TotalShoulderBashDamage: float
    TotalGrenadeDamage: float
    TotalPowerWeaponKills: int
    TotalPowerWeaponDamage: float
    TotalPowerWeaponGrabs: int
    TotalPowerWeaponPossessionTime: str
    TotalDeaths: int
    TotalAssists: int
    TotalGamesCompleted: int
    TotalGamesWon: int
    TotalGamesLost: int
    TotalGamesTied: int
    TotalTimePlayed: str
    TotalGrenadeKills: int
    MedalAwards: List[MedalAward]
    DestroyedEnemyVehicles: List[Any]
    EnemyKills: List[Any]
    WeaponStats: List[WeaponStats]
    Impulses: List[Impulse]
    TotalSpartanKills: int
    FastestMatchWin: str

class FlexibleStats(BaseModel):
    MedalStatCounts: List[FlexibleStatCount]
    ImpulseStatCounts: List[FlexibleStatCount]
    MedalTimelapses: List[Any]
    ImpulseTimelapses: List[ImpulseTimelapse]

class ArenaGameBaseVariantStats(BaseModel):
    FlexibleStats: FlexibleStats
    GameBaseVariantId: str
    TotalKills: int
    TotalHeadshots: int
    TotalWeaponDamage: float
    TotalShotsFired: int
    TotalShotsLanded: int
    WeaponWithMostKills: WeaponStats
    TotalMeleeKills: int
    TotalMeleeDamage: float
    TotalAssassinations: int
    TotalGroundPoundKills: int
    TotalGroundPoundDamage: float
    TotalShoulderBashKills: int
    TotalShoulderBashDamage: float
    TotalGrenadeDamage: float
    TotalPowerWeaponKills: int
    TotalPowerWeaponDamage: float
    TotalPowerWeaponGrabs: int
    TotalPowerWeaponPossessionTime: str
    TotalDeaths: int
    TotalAssists: int
    TotalGamesCompleted: int
    TotalGamesWon: int
    TotalGamesLost: int
    TotalGamesTied: int
    TotalTimePlayed: str
    TotalGrenadeKills: int
    MedalAwards: List[MedalAward]
    DestroyedEnemyVehicles: List[Any]
    EnemyKills: List[Any]
    WeaponStats: List[WeaponStats]
    Impulses: List[Impulse]
    TotalSpartanKills: int
    FastestMatchWin: str

class TopGameBaseVariant(BaseModel):
    GameBaseVariantRank: int
    NumberOfMatchesCompleted: int
    GameBaseVariantId: str
    NumberOfMatchesWon: int

class ArenaStats(BaseModel):
    ArenaPlaylistStats: List[ArenaPlaylistStats]
    HighestCsrAttained: Csr
    ArenaGameBaseVariantStats: List[ArenaGameBaseVariantStats]
    TopGameBaseVariants: List[TopGameBaseVariant]
    HighestCsrPlaylistId: str
    HighestCsrSeasonId: str
    ArenaPlaylistStatsSeasonId: str
    TotalKills: int
    TotalHeadshots: int
    TotalWeaponDamage: float
    TotalShotsFired: int
    TotalShotsLanded: int
    WeaponWithMostKills: WeaponStats
    TotalMeleeKills: int
    TotalMeleeDamage: float
    TotalAssassinations: int
    TotalGroundPoundKills: int
    TotalGroundPoundDamage: float
    TotalShoulderBashKills: int
    TotalShoulderBashDamage: float
    TotalGrenadeDamage: float
    TotalPowerWeaponKills: int
    TotalPowerWeaponDamage: float
    TotalPowerWeaponGrabs: int
    TotalPowerWeaponPossessionTime: str
    TotalDeaths: int
    TotalAssists: int
    TotalGamesCompleted: int
    TotalGamesWon: int
    TotalGamesLost: int
    TotalGamesTied: int
    TotalTimePlayed: str
    TotalGrenadeKills: int
    MedalAwards: List[MedalAward]
    DestroyedEnemyVehicles: List[Any]
    EnemyKills: List[Any]
    WeaponStats: List[WeaponStats]
    Impulses: List[Impulse]
    TotalSpartanKills: int
    FastestMatchWin: str

class PlayerId(BaseModel):
    Gamertag: str
    Xuid: Optional[str]

class ServiceRecordResultData(BaseModel):
    ArenaStats: ArenaStats
    PlayerId: PlayerId
    SpartanRank: int
    Xp: int

class ServiceRecordResult(BaseModel):
    Id: str
    ResultCode: int
    Result: ServiceRecordResultData

class LinkSelf(BaseModel):
    AuthorityId: str
    Path: str
    QueryString: str
    RetryPolicyId: str
    TopicName: str
    AcknowledgementTypeId: int
    AuthenticationLifetimeExtensionSupported: bool
    ClearanceAware: bool

class Links(BaseModel):
    Self: LinkSelf

class ServiceRecordResponse(BaseModel):
    Results: List[ServiceRecordResult]
    Links: Links
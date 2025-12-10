from pydantic import BaseModel

class Player(BaseModel):
    gamertag: str

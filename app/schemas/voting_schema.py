from pydantic import BaseModel
from datetime import datetime


class VoteRecord(BaseModel):
    request_id: str
    timestamp: datetime
    arthur_aguiar: int
    davi_brito: int
    yagami_light: int

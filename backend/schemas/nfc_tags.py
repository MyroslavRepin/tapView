import secrets
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NFCTagSchema(BaseModel):
    id: int
    uid: str
    redirect_url: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class NFCTagCreate(BaseModel):
    redirect_url: str


class NFCTagRead(BaseModel):
    id: int
    uid: str
    redirect_url: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

from fastapi import APIRouter, Depends
from sqlalchemy import schema
from sqlalchemy.orm import Session

from backend.deps.db import get_session
from backend.repo.nfc_tags import NFCTagRepo
from backend.schemas.nfc_tags import NFCTagCreate, NFCTagSchema

router = APIRouter()


@router.post("/api/nfc_tags", response_model=NFCTagSchema)
def create_nfc_tag(nfc_tag: NFCTagCreate, session: Session = Depends(get_session)):
    return NFCTagRepo.create(session=session, schema=nfc_tag)

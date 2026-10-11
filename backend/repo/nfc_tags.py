from sqlalchemy.orm import Session

from backend.models import nfc_tags
from backend.models.nfc_tags import NFCTag
from backend.schemas.nfc_tags import NFCTagSchema


class NFCTagRepo:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create(session: Session, schema: NFCTagSchema) -> NFCTag:
        nfc_tag = NFCTag(**schema.model_dump())
        session.add(nfc_tag)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        session.refresh(nfc_tag)
        return nfc_tag

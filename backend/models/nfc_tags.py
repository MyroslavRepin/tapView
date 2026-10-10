from sqlalchemy.orm import Mapped, mapped_column

from backend.core.base import Base


class NFC_tags(Base):
    __tablename__ = "nfc_tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(unique=True, nullable=False)
    redirect_url: Mapped[str] = mapped_column(nullable=False)

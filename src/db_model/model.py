import uuid
from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def generate_uuid():
    return str(uuid.uuid4())


class Game(db.Model):
    __tablename__ = "games"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    years: Mapped[List["GameYear"]] = relationship(
        "GameYear",
        back_populates="game",
        primaryjoin="Game.id == GameYear.game_id",
    )


class GameYear(db.Model):  # type: ignore
    __tablename__ = "game_years"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    game_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("games.id"), index=True, nullable=False
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    initial_state: Mapped[dict] = mapped_column(JSONB, nullable=False)
    actions: Mapped[dict] = mapped_column(JSONB, nullable=False)

    status: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    game: Mapped["Game"] = relationship(
        "Game",
        back_populates="years",
    )

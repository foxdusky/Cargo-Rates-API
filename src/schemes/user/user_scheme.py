from datetime import datetime

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    id: int | None = Field(primary_key=True)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    reg_at: datetime = Field(default_factory=datetime.utcnow)


class User(UserBase, table=True):
    __tablename__ = "user"

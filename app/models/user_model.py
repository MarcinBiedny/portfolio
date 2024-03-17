from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions.flask_sqlalchemy import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(120))

    def getName(self):
        return self.name

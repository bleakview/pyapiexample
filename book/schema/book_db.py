import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import UUIDType
from db.config import Base


class BookDB(Base):

    """Books model for SQLAlchemy DB"""
    __tablename__ = 'books'

    id = Column(UUIDType(), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    release_year = Column(Integer, nullable=False)
    isbn = Column(String(16), nullable=False)

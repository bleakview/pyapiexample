import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
# DB_CONNECTION_URL is not set use sqlite for database
DB_CONNECTION_URL = os.getenv(
    "DB_CONNECTION_URL", "sqlite+aiosqlite:///./book.db")

engine = create_async_engine(DB_CONNECTION_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

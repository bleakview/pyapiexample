from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from book.schema.book_db import BookDB


class DataAccessLayer():
    """Data Access Layer for Book"""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_book(self, name: str, author: str,   release_year: int, isbn: str, id: str = None):
        new_book = BookDB(id=id, name=name, author=author,
                          release_year=release_year, isbn=isbn)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_all_books(self) -> List[BookDB]:
        q = await self.db_session.execute(select(BookDB).order_by(BookDB.id))
        return q.scalars().all()

    async def get_book(self, book_id: str) -> List[BookDB]:
        q = await self.db_session.execute(select(BookDB).where(BookDB.id == book_id))
        return q.scalars().one()

    async def update_book(self, book_id: int, name: Optional[str], author: Optional[str], release_year: Optional[int], isbn: Optional[str]):
        q = update(BookDB).where(BookDB.id == book_id)
        if name:
            q = q.values(name=name)
        if author:
            q = q.values(author=author)
        if release_year:
            q = q.values(release_year=release_year)
        if isbn:
            q = q.values(isbn=isbn)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

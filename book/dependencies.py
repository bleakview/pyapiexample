"""fast API """
from db.config import async_session
from book.data_access_layer import DataAccessLayer


async def book_data_access_layer():
    async with async_session() as session:
        async with session.begin():
            yield DataAccessLayer(session)

import os
import uvicorn
from fastapi import FastAPI
from book.data_access_layer import DataAccessLayer

from db.config import engine, Base, async_session
from book import routers as book_router
from docs.docs import tags_metadata
from book.model.book_model import BookModel


description = """
This API handles books operations. 

## Operations

With this API you can:

* **Create book** 
* **Update book** 
* **Get all books**
* **Get specific book with {id}**

"""
app = FastAPI(
    title="Books DB application",
    description=description,
    version="0.0.1",
    contact={
        "name": "Mustafa Unal",
        "url": "https://github.com/bleakview/",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)
app.include_router(book_router.router)


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        async with async_session() as session:
            async with session.begin():
                # create test data
                test_data = BookModel(
                    name="name",
                    author="author",
                    isbn="isbn",
                    release_year=1980,
                )
                book_dal = DataAccessLayer(session)
                await book_dal.create_book(test_data.name, test_data.author, test_data.release_year, test_data.isbn, "5d596c01-e20b-4049-91e9-a0be77715260")


if "PYTEST_CURRENT_TEST" in os.environ:
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.drop_all)
        conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    PORT = os.getenv(
        "PORT", "8000")
    uvicorn.run("app:app", port=PORT, host='0.0.0.0')

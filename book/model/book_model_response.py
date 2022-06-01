from pydantic import BaseModel
from typing import Optional
from fastapi import Query
from uuid import UUID


class BookModelResponse(BaseModel):
    """Book Model Response for API"""
    id: UUID = Query(None, description="id book", )
    name: Optional[str] = Query(None, description="name of book", )
    author: Optional[str] = Query(None, description="books author", )
    release_year: Optional[int] = Query(
        None, description="book release year", )
    isbn: Optional[str] = Query(None, description="isbn number", )

    class Config:
        orm_mode = True

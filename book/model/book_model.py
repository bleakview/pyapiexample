from pydantic import BaseModel
from typing import Optional
from fastapi import Query


class BookModel(BaseModel):
    """Book Model for API"""
    name: Optional[str] = Query(None, description="name of book", )
    author: Optional[str] = Query(None, description="books author", )
    release_year: Optional[int] = Query(
        None, description="book release year", )
    isbn: Optional[str] = Query(None, description="isbn number", )

""" fast API router configuration for book"""
from typing import List

from fastapi import APIRouter, Depends, Query, Body

from book.data_access_layer import DataAccessLayer
from book.schema.book_db import BookDB
from book.dependencies import get_book_data_access_layer
from book.model.book_model import BookModel

router = APIRouter()


@router.post("/books", response_model=BookModel, tags=["post book"])
async def create_book(book: BookModel = Body(), book_data_access_layer: DataAccessLayer = Depends(get_book_data_access_layer)) -> BookModel:
    await book_data_access_layer.create_book(book.name, book.author, book.release_year, book.isbn)
    return book


@router.put("/books/{id}", tags=["put book"])
async def update_book(id: str = Query(description="book id", ), book: BookModel = Body(),
                      book_dal: DataAccessLayer = Depends(get_book_data_access_layer)):
    return await book_dal.update_book(id, book.name, book.author, book.release_year, book.isbn)


@router.get("/books", tags=["get books"])
async def get_all_books(book_dal: DataAccessLayer = Depends(get_book_data_access_layer)) -> List[BookDB]:
    return await book_dal.get_all_books()


@router.get("/books/{id}", tags=["get book"])
async def get_book(id: str = Query(description="book id", ), book_dal: DataAccessLayer = Depends(get_book_data_access_layer)) -> BookDB:
    return await book_dal.get_book(id)

""" fast API router configuration for book"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Body

from book.data_access_layer import DataAccessLayer
from book.model.book_model_response import BookModelResponse
from book.schema.book_db import BookDB
from book.dependencies import book_data_access_layer
from book.model.book_model_request import BookModelRequest

router = APIRouter()

# we use dedendency injection in this file with depends


@router.post("/books", response_model=BookModelResponse, tags=["post book"])
async def create_book(book: BookModelRequest = Body(),
                      book_data_access_layer: DataAccessLayer =
                      Depends(book_data_access_layer)) -> BookModelResponse:
    created_book = await book_data_access_layer.create_book(book.name,
                                                            book.author,
                                                            book.release_year,
                                                            book.isbn)
    print(create_book)
    return created_book


@router.put("/books/{id}", tags=["put book"])
async def update_book(id: str = Query(description="book id", ),
                      book: BookModelRequest = Body(),
                      book_dal:
                      DataAccessLayer = Depends(book_data_access_layer)):
    bookResult = await book_dal.update_book(id, book.name,
                                            book.author,
                                            book.release_year,
                                            book.isbn)
    if bookResult is False:
        raise HTTPException(status_code=404, detail="Item not found")


@router.get("/books",
            response_model=List[BookModelResponse],
            tags=["get books"])
async def get_all_books(book_dal:
                        DataAccessLayer =
                        Depends(book_data_access_layer)) -> List[BookDB]:
    return await book_dal.get_all_books()


@router.get("/books/{id}", response_model=BookModelResponse, tags=["get book"])
async def get_book(id: str = Query(description="book id", ),
                   book_dal: DataAccessLayer =
                   Depends(book_data_access_layer)) -> BookModelResponse:
    book = await book_dal.get_book(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return book

from typing import List
from fastapi import APIRouter, Response
from http import HTTPStatus
from app.data.cities_data_cursor import database_cursor

router = APIRouter()

tags = ['cities']


@router.get('/cities/', tags=tags, status_code=HTTPStatus.OK)
async def read_cities() -> List:
    """This function read all the cities present in the .JSON database"""
    return database_cursor()

from typing import List
from fastapi import APIRouter
from app.data.cities_data import database_cursor

router = APIRouter()

tags = ['cities']


@router.get('/cities/', tags=tags)
async def read_cities() -> List:
    return database_cursor()


@router.get('/cities/{state}', tags=tags)
async def read_cities_by_state(state: str):
    return database_cursor(state)

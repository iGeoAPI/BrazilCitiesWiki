from typing import List
from fastapi import APIRouter, Response
from http import HTTPStatus
from app.data.json_cursor import database_cursor


router = APIRouter()


end_point = 'states'

tags = ['states']


@router.get('/states/', tags=tags, status_code=HTTPStatus.OK)
async def read_cities() -> List:
    """This function read all the cities present in the .JSON database"""
    return database_cursor()


@router.get('/states/{state}', tags=tags, status_code=HTTPStatus.OK)
async def read_cities_by_state(state: str, response: Response):
    """This function read all the cities of a given state passed in as a path param"""
    router_response = database_cursor(state)
    if router_response:
        return router_response
    response.status_code = HTTPStatus.NOT_FOUND
    return {'msg': f'Invalid data'}

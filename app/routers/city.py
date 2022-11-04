from typing import List
from fastapi import APIRouter, Response
from http import HTTPStatus
from app.data.cities_data_cursor import json_cursor

router = APIRouter()

end_point = 'cities'

tags = [end_point]


# TODO: All the cities should be returned not the states
# TODO: A neat implementation of how to collect the cities must be set
@router.get('/cities/', tags=tags, status_code=HTTPStatus.OK)
async def read_cities() -> List:
    """This function read all the cities present in the .JSON database"""
    return json_cursor(scope=end_point)

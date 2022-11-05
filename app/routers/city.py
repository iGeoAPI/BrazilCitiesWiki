from typing import List, Optional
from http import HTTPStatus
from app.schemas import CityIn
from app.data.cities_data_cursor import json_cursor


from fastapi import APIRouter, Response


router = APIRouter()

end_point = 'cities'

tags = [end_point]


# TODO: All the cities should be returned not the states
# TODO: A neat implementation of how to collect the cities must be set
@router.get('/cities/', tags=tags, status_code=HTTPStatus.OK)
async def read_cities() -> List:
    """This function read all the cities present in the .JSON database"""
    return json_cursor(scope=end_point)


@router.post('/cities/{name}', tags=tags, status_code=HTTPStatus.OK)
async def read_cities_by_name(city: CityIn, name: str = None, response: Response = None):
    """This function read all the cities of a given state passed in as a path param"""
    city = city.dict()
    router_response = json_cursor(city, name, scope=end_point)
    if router_response:
        return router_response
    response.status_code = HTTPStatus.NOT_FOUND
    return {'msg': f'Invalid data'}

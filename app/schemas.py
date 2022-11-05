from pydantic import BaseModel, Field


class CityOut(BaseModel):
    flag: str = Field(default=None, description='City flag')
    motto: str = Field(default=None, description='City motto')
    blazon: str = Field(default=None, description='City blazon')
    zip_range: str = Field(default=None, description='Zip range')
    name: str = Field(default=None, description='Name of the city')
    anthem: str = Field(default=None, description='The city anthem')
    total_area: int = Field(default=None, description='Total area km²')
    federative_unit: str = Field(default=None, description='Federative Unit/State')
    ibge_code: int = Field(default=None, description='Brazilian Institute of Geography and Statistics')


class CityIn(BaseModel):
    federative_unit: str = Field(default=None, description='Federative Unit/State')

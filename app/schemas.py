from pydantic import BaseModel, Field


class URL(BaseModel):
    url_address: str = Field(default=None)


class City(BaseModel):
    name: str = Field(default=None, description='Name of the city')
    ibge_code: str = Field(default=None, description='Brazilian Institute of Geography and Statistics')
    motto: str = Field(default=None, description='City motto')
    zip_range: str = Field(default=None, description='Zip range')
    anthem: str = Field(default=None, description='The city anthem')
    total_area: int = Field(default=None, description='Total area km²')
    flag: URL = Field(default=None, description='City flag')
    blazon: URL = Field(default=None, description='City blazon')

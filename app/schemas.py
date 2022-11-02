from pydantic import BaseModel, Field


class City(BaseModel):
    ibge_code: int = Field(default=None, description='Brazilian Institute of Geography and Statistics')
    name: str = Field(default=None, description='Name of the city')
    federative_unit: str = Field(default=None, description='Federative Unit/State')
    motto: str = Field(default=None, description='City motto')
    zip_range: str = Field(default=None, description='Zip range')
    anthem: str = Field(default=None, description='The city anthem')
    flag: str = Field(default=None, description='City flag')
    blazon: str = Field(default=None, description='City blazon')
    total_area: int = Field(default=None, description='Total area km²')

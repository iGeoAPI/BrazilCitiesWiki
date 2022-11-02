from fastapi import FastAPI
import uvicorn
from app.routers import city


app = FastAPI()


app.include_router(city.router)


@app.get('/')
async def root():
    # TODO: This needs to be changed to the homepage of the documentation on how to use this API
    return {'msg': 'This is the homepage'}

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)

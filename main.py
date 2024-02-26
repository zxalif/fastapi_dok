from fastapi import FastAPI
from app.utils import api


app = FastAPI()

@app.get('/')
def index():
    return {'msg': 'Ok'}


@app.get('/healtha')
def index():
    return {'msg': 'Ok'}


@app.get('/api')
async def api_Get():
    return api()

from fastapi import FastAPI
from routes import biak
from db import meta,engine

app = FastAPI()
meta.create_all(engine)
app.include_router(biak)

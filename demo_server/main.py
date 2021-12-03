import logging

import uvicorn

from demo_server import model
from demo_server.controller import create_routes
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from demo_server.database import Base, engine

logging.basicConfig()
logger = logging.getLogger(__name__)

app = FastAPI()


Base.metadata.create_all(engine)


app.mount("/static", StaticFiles(directory="resources/static"), name="static")

templates = Jinja2Templates(directory="resources/templates")

create_routes(app, templates)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

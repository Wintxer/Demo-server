import logging
from typing import Optional
from demo_server.controller import create_routes
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

logging.basicConfig()
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="resources/static"), name="static")

templates = Jinja2Templates(directory="resources/templates")

create_routes(app, templates)

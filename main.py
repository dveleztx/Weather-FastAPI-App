#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 04/27/2021
# Description : Weather API Application
###############################################################################

# Imports
import fastapi
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# API Object and Webserver Configuration
api = fastapi.FastAPI()
config = Config()
config.bind = ["localhost:8080"]

# Templates
templates = Jinja2Templates('templates')


@api.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


if __name__ == "__main__":
    asyncio.run(serve(api, config))

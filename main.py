#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 04/27/2021
# Description : Weather API Application
###############################################################################

# Imports
import fastapi
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# API Object and Webserver Configuration
api = fastapi.FastAPI(debug=True)

# Templates
templates = Jinja2Templates(directory='templates')


@api.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")

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
from starlette.staticfiles import StaticFiles

# Custom Imports
from api import weather_api
from views import home


# API Object and Webserver Configuration
api = fastapi.FastAPI(debug=True)


def configure():
    configure_router()


def configure_router():
    # Templates and Static Files
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()

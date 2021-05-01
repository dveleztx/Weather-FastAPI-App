#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 04/27/2021
# Description : Weather API Application
###############################################################################

# Imports
import json
import fastapi
import uvicorn
from pathlib import Path
from starlette.staticfiles import StaticFiles
# Custom Imports
from api import weather_api
from services import openweather_service
from views import home


# API Object and Webserver Configuration
api = fastapi.FastAPI(debug=True)


def configure():
    configure_router()
    configure_api_keys()


def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")

    with open("settings.json") as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")


def configure_router():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()

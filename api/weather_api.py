# Imports
import fastapi
from fastapi import Depends
from typing import Optional, List
# Custom Imports
from models.location import Location
from models.reports import Report
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as ex:
        print(f"Server crashed while processing request: {ex}")
        return fastapi.Response(content="Error processing your request.", status_code=500)


@router.get("/api/reports", name="all_reports")
async def reports_get() -> List[Report]:
    # await report_service.add_report("A", Location(city="San Antonio"))
    # await report_service.add_report("B", Location(city="Austin"))
    return await report_service.get_reports()


# Imports
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
# Custom Imports
from models.location import Location


class Report(BaseModel):
    description: str
    location: Location
    created_date: Optional[datetime]

from datetime import datetime
from pydantic import BaseModel


class GoodIn(BaseModel):
    id = int
    name = str
    price = float
    manufacture_date = datetime
    picture_url = str

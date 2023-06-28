from datetime import date
from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class GoodIn(BaseModel):
    # id = int
    name: str = "Kakao"
    price: float = 2.5
    manufacture_date: date | None
    picture_url: str | None = r"pics.com/kakao.jpg"


class OrderGood(BaseModel):
    good_id: int
    ammount: int

    @validator('ammount')
    def ammount_positive(cls, v):
        assert v > 0, 'must be positive'
        return v


class OrderIn(BaseModel):
    order_date: date
    customer_name: str
    customer_email: EmailStr | None
    delivery_address: str | None
    notes: str | None
    status: str | None
    good_item: list[OrderGood]

class TokenData(BaseModel):
    email: Optional[str] = None

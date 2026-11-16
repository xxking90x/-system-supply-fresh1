from pydantic import BaseModel
import datetime

class ProductCreate(BaseModel):
    sku: str
    name: str
    category: str
    quantity: int
    max_temperature: float
    expiry_date: datetime.datetime

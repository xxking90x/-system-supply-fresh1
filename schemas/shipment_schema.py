from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    product_id: int
    origin: str
    destination: str
    current_temperature: float

class TemperatureUpdate(BaseModel):
    current_temperature: float

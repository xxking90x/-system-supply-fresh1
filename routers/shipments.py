from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.shipment_schema import ShipmentCreate, TemperatureUpdate
from services.logistic_service import LogisticService

router = APIRouter()
@router.post("/create")
def create_shipment(shipment: ShipmentCreate, db: Session = Depends(get_db)):
    return LogisticService.create_shipment(db, shipment)

@router.put("/{shipment_id}/update-temp")
def update_shipment_temp(shipment_id: int, temp_data: TemperatureUpdate, db: Session = Depends(get_db)):
    return LogisticService.update_temperature(db, shipment_id, temp_data.current_temperature)

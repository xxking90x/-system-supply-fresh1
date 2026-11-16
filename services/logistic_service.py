from sqlalchemy.orm import Session
from models.shipment import ShipmentModel
from schemas.shipment_schema import ShipmentCreate
from services.inventory_service import InventoryService
from fastapi import HTTPException

class LogisticService:
    @staticmethod
    def create_shipment(db: Session, shipment_data: ShipmentCreate):
        new_shipment = ShipmentModel(**shipment_data.dict())
        db.add(new_shipment)
        db.commit()
        db.refresh(new_shipment)
        return new_shipment

    @staticmethod
    def update_temperature(db: Session, shipment_id: int, new_temp: float):
        shipment = db.query(ShipmentModel).filter(ShipmentModel.id == shipment_id).first()
        if not shipment:
            raise HTTPException(status_code=404, detail="الشحنة غير موجودة.")
        shipment.current_temperature = new_temp
        audit_result = InventoryService.audit_storage_conditions(db, shipment.product_id, new_temp)
        if audit_result.get("status") == "ALERT":
            shipment.status = "DAMAGED"
        db.commit()
        return {"shipment_status": shipment.status, "audit_details": audit_result}

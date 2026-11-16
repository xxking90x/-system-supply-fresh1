from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.product_schema import ProductCreate
from services.inventory_service import InventoryService

router = APIRouter()
@router.post("/register-product")
def register_product(product: ProductCreate, db: Session = Depends(get_db)):
    return InventoryService.register_product(db, product)

@router.get("/audit-temp/{product_id}")
def check_temperature(product_id: int, current_temp: float, db: Session = Depends(get_db)):
    return InventoryService.audit_storage_conditions(db, product_id, current_temp)

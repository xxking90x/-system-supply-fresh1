from sqlalchemy.orm import Session
from models.product import ProductModel
from schemas.product_schema import ProductCreate
from fastapi import HTTPException, status
import datetime

class InventoryService:
    @staticmethod
    def register_product(db: Session, product_data: ProductCreate):
        existing = db.query(ProductModel).filter(ProductModel.sku == product_data.sku).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="المنتج بهذا الرمز مسجل مسبقاً في النظام."
            )
        db_product = ProductModel(
            sku=product_data.sku, name=product_data.name, category=product_data.category,
            quantity=product_data.quantity, max_temperature=product_data.max_temperature,
            expiry_date=product_data.expiry_date
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def audit_storage_conditions(db: Session, product_id: int, current_temp: float):
        product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="المنتج غير موجود.")
        if current_temp > product.max_temperature:
            return {
                "status": "ALERT",
                "message": f"تحذير هندسي: تجاوزت درجة الحرارة الحد المسموح للمنتج {product.name}!"
            }
        return {
            "status": "NORMAL", "message": "حالة التخزين مطابقة للمعايير القياسية.",
            "current_temp": current_temp, "max_allowed": product.max_temperature
        }

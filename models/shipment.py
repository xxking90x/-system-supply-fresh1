from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from core.database import Base
import datetime

class ShipmentModel(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    current_temperature = Column(Float, nullable=False)
    status = Column(String, default="IN_TRANSIT")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

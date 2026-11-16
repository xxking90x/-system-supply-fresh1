from fastapi import FastAPI
from core.database import engine, Base
from routers import auth, inventory, shipments

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FreshSupply Core Workflow System",
    description="نظام هندسي متكامل لإدارة سلاسل الإمداد والتخزين الذكي",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication & RBAC"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory Workflow"])
app.include_router(shipments.router, prefix="/api/shipments", tags=["Logistics & Tracking"])

@app.get("/")
def read_root():
    return {"message": "مرحباً بك في نظام هندسة البرمجيات التطبيقي - FreshSupply Core"}

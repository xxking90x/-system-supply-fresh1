def test_register_product_success(client):
    response = client.post("/api/inventory/register-product", json={
        "sku": "TOMATO-01", "name": "طماطم عضوية", "category": "خضروات",
        "quantity": 500, "max_temperature": 10.0, "expiry_date": "2027-12-31T00:00:00"
    })
    assert response.status_code == 200
    assert response.json()["sku"] == "TOMATO-01"

def test_register_product_duplicate_error(client):
    response = client.post("/api/inventory/register-product", json={
        "sku": "TOMATO-01", "name": "طماطم عضوية", "category": "خضروات",
        "quantity": 500, "max_temperature": 10.0, "expiry_date": "2027-12-31T00:00:00"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "المنتج بهذا الرمز مسجل مسبقاً في النظام."

def test_audit_temperature_normal(client):
    response = client.get("/api/inventory/audit-temp/1?current_temp=8.0")
    assert response.status_code == 200
    assert response.json()["status"] == "NORMAL"

def test_audit_temperature_alert(client):
    response = client.get("/api/inventory/audit-temp/1?current_temp=12.5")
    assert response.status_code == 200
    assert response.json()["status"] == "ALERT"
    assert "تجاوزت درجة الحرارة" in response.json()["message"]

def test_create_shipment(client):
    response = client.post("/api/shipments/create", json={
        "product_id": 1, "origin": "المزرعة A", "destination": "المستودع الرئيسي",
        "current_temperature": 5.0
    })
    assert response.status_code == 200
    assert response.json()["status"] == "IN_TRANSIT"

def test_update_shipment_temperature_damage(client):
    response = client.put("/api/shipments/1/update-temp", json={
        "current_temperature": 15.0
    })
    assert response.status_code == 200
    assert response.json()["shipment_status"] == "DAMAGED"

def test_update_shipment_not_found_error(client):
    response = client.put("/api/shipments/999/update-temp", json={
        "current_temperature": 10.0
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "الشحنة غير موجودة."

import json
from app.api import app

def test_api_precio_final():
    cliente = app.test_client()
    payload = {
        "precio": 100,
        "cupon": "OFERTA10",
        "impuesto": 0.19
    }
    response = cliente.post("/precio", data=json.dumps(payload), content_type='application/json')
    data = response.get_json()
    assert response.status_code == 200
    assert data["precio_final"] == 107.1

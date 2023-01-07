def test_get_app_info(flask_client):
    response = flask_client.get("/api/info", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.get_json()["Git-Branch"]

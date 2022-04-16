"""Tests debug file"""

def test_debug_file(client):
    response = client.get("/logs")
    assert response.status_code == 200
    assert b"Add" in response.data

"""Tests request log file is created"""
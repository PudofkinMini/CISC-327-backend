#https://fastapi.tiangolo.com/tutorial/testing/
#I used "pytest -r test_main.py >>firstoutput.txt" to run the quick output and print to file.
#https://docs.pytest.org/en/6.2.x/usage.html Here is a list of available flags
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_test_setupSuccess():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_test_setupFailure():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}
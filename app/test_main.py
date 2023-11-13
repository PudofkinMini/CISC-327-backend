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

#####################################################################

# Parameters : restaurant_id = 48 (Lonestar)  
def test_test_loadMenu1():
    response = client.get("/loadMenu/48")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

# Parameters : restaurant_id = 57 (Olivea)
def test_test_loadMenu2():
    response = client.get("/loadMenu/57")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

# Parameters : restaurant_id = 22 (Non-existant)
def test_test_loadMenu3():
    response = client.get("/loadMenu/22")
    assert response.status_code == 200
    assert response.json() == []

#####################################################################    

'''
Parameters : user_id = 2
             restaurant_id = 44
             order_id = 12
'''
def test_test_placeOrder1():
    response = client.get("/payAndPlaceOrder/2/44/12")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

'''
Parameters : user_id = 2
             restaurant_id = 46
             order_id = 15
'''
def test_test_placeOrder2():
    response = client.get("/payAndPlaceOrder/2/46/15")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

'''
Parameters : user_id = 2
             restaurant_id = 58
             order_id = 10 (Non-Existant)
'''
def test_test_placeOrder3():
    response = client.get("/payAndPlaceOrder/2/58/10")
    assert response.status_code == 200
    assert response.json() == []
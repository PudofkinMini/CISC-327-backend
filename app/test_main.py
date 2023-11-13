#https://fastapi.tiangolo.com/tutorial/testing/
#I used "pytest -r test_main.py >>firstoutput.txt" to run the quick output and print to file.
#https://docs.pytest.org/en/6.2.x/usage.html Here is a list of available flags
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

####################################################################
#INITIAL PYTEST TEST RUN
####################################################################
def test_test_setupSuccess():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_test_setupFailure():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

###################################################################
#USER REGISTRATION/LOGIN                                          
###################################################################
def test_login_username(): #log in with existing username as input
    response = client.get("/login/admin/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has userid 2

def test_login_email(): #log in with existing email as input of same user --swappable credentials for same user
    response = client.get("/login/admin@email.com/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has user id 2. Must match

def test_login_username_DNE(): #Test DNE username login (DNE = Does Not Exist)
    response = client.get("/login/fakeemail@gmail.net/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""}

def test_login_email_DNE(): #Test DNE email login (DNE = Does Not Exist)
    response = client.get("/login/fakeUser/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""}

#####################################################################
#LoadMenu testing
#####################################################################
# Parameters : restaurant_id = 48 (Lonestar)  
def test_loadMenu1():
    response = client.get("/loadMenu/48")
    assert response.status_code == 200
    parseMenu = response.json()
    assert len(parseMenu) == 8 #Lonestar should load 8 menu items
# Parameters : restaurant_id = 57 (Olivea)
def test_loadMenu2():
    response = client.get("/loadMenu/57")
    assert response.status_code == 200
    parseMenu = response.json()
    assert len(parseMenu) == 8 #Olivea should load 8 menu items

# Parameters : restaurant_id = 22 (Non-existant)
def test_loadMenuDNE():
    response = client.get("/loadMenu/22")
    assert response.status_code == 200
    parseMenu = response.json()
    assert len(parseMenu) == 0 #Should be an empty json body

#####################################################################    

'''
Parameters : user_id = 2
             restaurant_id = 44
             order_id = 12
'''
def test_placeOrder1():
    response = client.get("/payAndPlaceOrder/2/44/12")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

'''
Parameters : user_id = 2
             restaurant_id = 46
             order_id = 15
'''
def test_placeOrder2():
    response = client.get("/payAndPlaceOrder/2/46/15")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

'''
Parameters : user_id = 2
             restaurant_id = 58
             order_id = 10 (Non-Existant)
'''
def test_placeOrderDNE(): #SQL Server side failure
    response = client.get("/payAndPlaceOrder/2/58/10")
    assert response.status_code == 500
    assert response.json() == []
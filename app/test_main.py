#https://fastapi.tiangolo.com/tutorial/testing/
#I used "pytest -r test_main.py >>firstoutput.txt" to run the quick output and print to file.
#https://docs.pytest.org/en/6.2.x/usage.html Here is a list of available flags
from fastapi.testclient import TestClient
from unittest import TestCase
from .main import app

client = TestClient(app)

####################################################################
#INITIAL PYTEST TEST RUN
####################################################################
'''def test_test_setupSuccess():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_test_setupFailure():
    response = client.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}
'''
###################################################################
#USER REGISTRATION TESTING                                    
###################################################################
def test_registration_clean(): #register with new email, username, and password (Parameters: email = anotherneew@email.com, username = neweUser, password=12345678longPassword)
    response = client.get("/register/anotherneew@email.com/neweUser/12345678longPassword")
    assert response.status_code == 200
    assert response.json() == {'success': 'true'} 

def test_registration_already_exists(): #register with existing username, email, password (Parameters: email = admin@email.com, username = admin, password=12345678longPassword)
    response = client.get("/register/admin@email.com/admin/12345678longPassword")
    assert response.status_code == 200
    assert response.json() == {'success': 'false', 'reason': 'Account with same username or email already exists'} 

def test_registration_too_short(): #register with password less than 8 characters (Parameters: email = anotherneew@email.com, username = neweUser, password=3)
    response = client.get("/register/anotherneew@email.com/neweUser/3")
    assert response.status_code == 200
    assert response.json() == {'success': 'false', 'reason': 'Password must be at least 8 characters long.'} 

###################################################################
#USER LOGIN TESTING                                         
###################################################################
def test_login_username(): #log in with existing username as input (Parameters : username = admin, password = password)
    response = client.get("/login/admin/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has userid 2

def test_login_email(): #log in with existing email as input of same user --swappable credentials for same user (Parameters : username = admin@email.com, password = password)
    response = client.get("/login/admin@email.com/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has user id 2. Must match

def test_login_username_DNE(): #Test DNE username login (DNE = Does Not Exist) (Parameters : username = fakeemail@gmal.com, password = diffPassword)
    response = client.get("/login/fakeemail@gmail.net/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""} #empty, no user exists

def test_login_email_DNE(): #Test DNE email login (DNE = Does Not Exist) (Parameters : username = fakeUser, password = diffPassword)
    response = client.get("/login/fakeUser/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""} #empty, no user exists

#####################################################################
#LoadMenu TESTING
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
# P   placeOrder TESTING (Combined with make payments--handled simultaneously)
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

def test_placeOrderDNE(): #SQL Server side failure
    response = client.get("/payAndPlaceOrder/2/58/10")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
'''

#####################################################################
# P   loadOrders TESTING 
#####################################################################

'''
Parameters : user_id = 2
'''
def test1_loadOrders(user_id): 
    response = client.get("/loadOrders/2")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

#####################################################################
# EXHAUSTIVE TESTING FOR LOAD RESTAURANTS (Unit Testing)
#####################################################################
def test_loadRestaurantsComfort():
    response = client.get("/loadRestaurants/Comfort")
    comfort_rest_list = [{'id': 47, 'name': 'Pizza Hut', 'category': 'Comfort', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.090000', 'updated': '2023-11-01T18:59:48.090000', 'deleted': None}, {'id': 48, 'name': 'Lonestar', 'category': 'Comfort', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.220000', 'updated': '2023-11-01T18:59:48.220000', 'deleted': None}, {'id': 49, 'name': 'Osmows', 'category': 'Comfort', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.360000', 'updated': '2023-11-01T18:59:48.360000', 'deleted': None}]
    assert response.status_code == 200
    assert comfort_rest_list == response.json()

def test_loadRestaurantsIndian():
    response = client.get("/loadRestaurants/Comfort")
    comfort_indian_list = [{'id': 47, 'name': 'Pizza Hut', 'category': 'Comfort', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.090000', 'updated': '2023-11-01T18:59:48.090000', 'deleted': None}, {'id': 48, 'name': 'Lonestar', 'category': 'Comfort', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.220000', 'updated': '2023-11-01T18:59:48.220000', 'deleted': None}, {'id': 49, 'name': 'Osmows', 'category': 'Comfort', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.360000', 'updated': '2023-11-01T18:59:48.360000', 'deleted': None}]
    assert response.status_code == 200
    assert comfort_rest_list == response.json()
    
    
def test_loadRestaurantsComfort():
    response = client.get("/loadRestaurants/Comfort")
    comfort_rest_list = [{'id': 47, 'name': 'Pizza Hut', 'category': 'Comfort', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.090000', 'updated': '2023-11-01T18:59:48.090000', 'deleted': None}, {'id': 48, 'name': 'Lonestar', 'category': 'Comfort', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.220000', 'updated': '2023-11-01T18:59:48.220000', 'deleted': None}, {'id': 49, 'name': 'Osmows', 'category': 'Comfort', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.360000', 'updated': '2023-11-01T18:59:48.360000', 'deleted': None}]
    assert response.status_code == 200
    assert comfort_rest_list == response.json()

def test_loadRestaurantsComfort():
    response = client.get("/loadRestaurants/Comfort")
    comfort_rest_list = [{'id': 47, 'name': 'Pizza Hut', 'category': 'Comfort', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.090000', 'updated': '2023-11-01T18:59:48.090000', 'deleted': None}, {'id': 48, 'name': 'Lonestar', 'category': 'Comfort', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.220000', 'updated': '2023-11-01T18:59:48.220000', 'deleted': None}, {'id': 49, 'name': 'Osmows', 'category': 'Comfort', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.360000', 'updated': '2023-11-01T18:59:48.360000', 'deleted': None}]
    assert response.status_code == 200
    assert comfort_rest_list == response.json()
    
def test_loadRestaurantsChinese():
    response = client.get("/loadRestaurants/Chinese")
    chinese_rest_list = [{'id': 50, 'name': 'Mandarin', 'category': 'Chinese', 'price': '$', 'logo': None, 'created': '2023-11-01 18:59:48.493', 'updated': '2023-11-01 18:59:48.493', 'deleted': None}, 
                   {'id': 51, 'name': 'VIP Chinese Restaurant', 'category': 'Chinese', 'price': '$$', 'logo': None, 'created': '2023-11-01 18:59:48.623', 'updated': '2023-11-01 18:59:48.623', 'deleted': None}, 
                   {'id': 52, 'name': 'Yellow River', 'category': 'Chinese', 'price': '$$$', 'logo': None, 'created': '2023-11-01 18:59:48.773', 'updated': '2023-11-01 18:59:48.773', 'deleted': None}]
    assert response.status_code == 200
    assert chinese_rest_list == response.json()
    
def test_loadRestaurantsFastFood():
    response = client.get("/loadRestaurants/Fast Food")
    fastFood_rest_list = [{'id': 50, 'name': 'Mandarin', 'category': 'Chinese', 'price': '$', 'logo': None, 'created': '2023-11-01 18:59:48.493', 'updated': '2023-11-01 18:59:48.493', 'deleted': None}, 
                   {'id': 51, 'name': 'VIP Chinese Restaurant', 'category': 'Chinese', 'price': '$$', 'logo': None, 'created': '2023-11-01 18:59:48.623', 'updated': '2023-11-01 18:59:48.623', 'deleted': None}, 
                   {'id': 52, 'name': 'Yellow River', 'category': 'Chinese', 'price': '$$$', 'logo': None, 'created': '2023-11-01 18:59:48.773', 'updated': '2023-11-01 18:59:48.773', 'deleted': None}]
    assert response.status_code == 200
    assert fastFood_rest_list == response.json()

def test_loadRestaurantsItalian():
    response = client.get("/loadRestaurants/Italian")
    italian_rest_list = [{'id': 50, 'name': 'Mandarin', 'category': 'Chinese', 'price': '$', 'logo': None, 'created': '2023-11-01 18:59:48.493', 'updated': '2023-11-01 18:59:48.493', 'deleted': None}, 
                   {'id': 51, 'name': 'VIP Chinese Restaurant', 'category': 'Chinese', 'price': '$$', 'logo': None, 'created': '2023-11-01 18:59:48.623', 'updated': '2023-11-01 18:59:48.623', 'deleted': None}, 
                   {'id': 52, 'name': 'Yellow River', 'category': 'Chinese', 'price': '$$$', 'logo': None, 'created': '2023-11-01 18:59:48.773', 'updated': '2023-11-01 18:59:48.773', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()

#####################################################################
# Add to Cart | Data-Centric Partitioning | (Unit Testing)
#####################################################################    
def test_add_to_empty_cart():
    response = client.get("/addToCart/2/62/150")
    assert response.status_code == 200
    
    
def test_add_to_1_item_cart():
    response = client.get("/addToCart/2/62/151")
    assert response.status_code == 200
    

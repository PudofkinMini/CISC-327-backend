''' HEADER FOR FILE

THIS IS THE DAILY TESTING SUITE FOR THE BACKEND OF OUR APPLICATION
IT TESTS ALL DAY-TO-DAY CRITICAL MAJOR STATE-CHANGING FUNCTIONALITY WITHIN THE APPLICATION
WE ARE USING TESTCLIENT FROM FASTAPI LIBRARY TO CONDUCT TEST API REQUESTS
WE ARE USING PYTEST TO DISPLAY AND ASSERT OUR TEST CASES
'''


#https://fastapi.tiangolo.com/tutorial/testing/
#pytest app/test_daily.py
#https://docs.pytest.org/en/6.2.x/usage.html Here is a list of available flags
from fastapi.testclient import TestClient
from unittest import TestCase
from .main import app

dailyTestClient = TestClient(app)

####################################################################
#INITIAL PYTEST TEST RUN
####################################################################
'''def test_test_setupSuccess():
    response = dailyTestClient.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_test_setupFailure():
    response = dailyTestClient.get("/testSetup")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}
'''

###################################################################
#USER LOGIN TESTING                                         
###################################################################
def test_login_username(): #log in with existing username as input (Parameters : username = admin, password = password)
    response = dailyTestClient.get("/login/admin/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has userid 2

def test_login_email(): #log in with existing email as input of same user --swappable credentials for same user (Parameters : username = admin@email.com, password = password)
    response = dailyTestClient.get("/login/admin@email.com/password")
    assert response.status_code == 200
    assert response.json() == {"userid": "2"} #admin has user id 2. Must match

def test_login_username_DNE(): #Test DNE username login (DNE = Does Not Exist) (Parameters : username = fakeemail@gmal.com, password = diffPassword)
    response = dailyTestClient.get("/login/fakeemail@gmail.net/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""} #empty, no user exists

def test_login_email_DNE(): #Test DNE email login (DNE = Does Not Exist) (Parameters : username = fakeUser, password = diffPassword)
    response = dailyTestClient.get("/login/fakeUser/diffPassword")
    assert response.status_code == 200
    assert response.json() == {"userid": ""} #empty, no user exists

#####################################################################
#LoadMenu TESTING
#####################################################################

# Parameters : restaurant_id = 48 (Lonestar)  
def test_loadMenu1():
    response = dailyTestClient.get("/loadMenu/48")
    assert response.status_code == 200
    parseMenu = response.json()
    assert len(parseMenu) == 8 #Lonestar should load 8 menu items
# Parameters : restaurant_id = 57 (Olivea)
def test_loadMenu2():
    response = dailyTestClient.get("/loadMenu/57")
    assert response.status_code == 200
    parseMenu = response.json()
    assert len(parseMenu) == 8 #Olivea should load 8 menu items

# Parameters : restaurant_id = 22 (Non-existant)
def test_loadMenuDNE():
    response = dailyTestClient.get("/loadMenu/22")
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
    response = dailyTestClient.get("/payAndPlaceOrder/2/44/12")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

'''
Parameters : user_id = 2
             restaurant_id = 46
             order_id = 15
'''
def test_placeOrder2():
    response = dailyTestClient.get("/payAndPlaceOrder/2/46/15")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

'''
Parameters : user_id = 2
             restaurant_id = 58
             order_id = 10 (Non-Existant)
'''
def test_placeOrderDNE(): 
    response = dailyTestClient.get("/payAndPlaceOrder/2/58/10")
    assert response.status_code == 200
    assert response.json() == {"status": "unsuccessful"}


#####################################################################
# P   loadOrders TESTING 
#####################################################################

'''
Parameters : user_id = 2
'''
def test1_loadOrders(): 
    response = dailyTestClient.get("/loadOrders/2")
    assert response.status_code == 200
    assert len(response.json()) == 10

#####################################################################
# EXHAUSTIVE TESTING FOR LOAD RESTAURANTS (Unit Testing)
#####################################################################
def test_loadRestaurantsComfort():
    response = dailyTestClient.get("/loadRestaurants/Comfort")
    comfort_rest_list = [{'id': 47, 'name': 'Pizza Hut', 'category': 'Comfort', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.090000', 'updated': '2023-11-01T18:59:48.090000', 'deleted': None}, {'id': 48, 'name': 'Lonestar', 'category': 'Comfort', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.220000', 'updated': '2023-11-01T18:59:48.220000', 'deleted': None}, {'id': 49, 'name': 'Osmows', 'category': 'Comfort', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.360000', 'updated': '2023-11-01T18:59:48.360000', 'deleted': None}]
    assert response.status_code == 200
    assert comfort_rest_list == response.json()

def test_loadRestaurantsIndian():
    response = dailyTestClient.get("/loadRestaurants/Indian")
    indian_rest_list = [{'id': 53, 'name': 'Tasty Indian Bar & Grill', 'category': 'Indian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.910000', 'updated': '2023-11-01T18:59:48.910000', 'deleted': None}, {'id': 54, 'name': 'Namaste Kingston', 'category': 'Indian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.040000', 'updated': '2023-11-01T18:59:49.040000', 'deleted': None}, {'id': 55, 'name': 'Flavours of India', 'category': 'Indian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.173000', 'updated': '2023-11-01T18:59:49.173000', 'deleted': None}]
    assert response.status_code == 200
    assert indian_rest_list == response.json()
    
    
def test_loadRestaurantsFrench():
    response = dailyTestClient.get("/loadRestaurants/French")
    french_rest_list = [{'id': 59, 'name': 'Geneva Crêpe Bistro', 'category': 'French', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.733000', 'updated': '2023-11-01T18:59:49.733000', 'deleted': None}, {'id': 60, 'name': 'Chez Piggy', 'category': 'French', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.863000', 'updated': '2023-11-01T18:59:49.863000', 'deleted': None}, {'id': 61, 'name': 'Bistro Stefan', 'category': 'French', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:50', 'updated': '2023-11-01T18:59:50', 'deleted': None}]
    assert response.status_code == 200
    assert french_rest_list == response.json()

def test_loadRestaurantsVegetarian():
    response = dailyTestClient.get("/loadRestaurants/Vegetarian")
    veg_rest_list = [{'id': 62, 'name': 'Freshii', 'category': 'Vegetarian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:50.127000', 'updated': '2023-11-01T18:59:50.127000', 'deleted': None}, {'id': 63, 'name': 'Atomica', 'category': 'Vegetarian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:50.270000', 'updated': '2023-11-01T18:59:50.270000', 'deleted': None}, {'id': 64, 'name': 'Copper Branch', 'category': 'Vegetarian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:50.413000', 'updated': '2023-11-01T18:59:50.413000', 'deleted': None}]
    assert response.status_code == 200
    assert veg_rest_list == response.json()
    
def test_loadRestaurantsChinese():
    response = dailyTestClient.get("/loadRestaurants/Chinese")
    chinese_rest_list = [{'id': 50, 'name': 'Mandarin', 'category': 'Chinese', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:48.493000', 'updated': '2023-11-01T18:59:48.493000', 'deleted': None}, {'id': 51, 'name': 'VIP Chinese Restaurant', 'category': 'Chinese', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:48.623000', 'updated': '2023-11-01T18:59:48.623000', 'deleted': None}, {'id': 52, 'name': 'Yellow River', 'category': 'Chinese', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:48.773000', 'updated': '2023-11-01T18:59:48.773000', 'deleted': None}]
    assert response.status_code == 200
    assert chinese_rest_list == response.json()
    
def test_loadRestaurantsFastFood():
    response = dailyTestClient.get("/loadRestaurants/Fast Food")
    fastFood_rest_list = [{'id': 44, 'name': "McDonald's", 'category': 'Fast Food', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:47.673000', 'updated': '2023-11-01T18:59:47.673000', 'deleted': None}, {'id': 45, 'name': 'Five Guys', 'category': 'Fast Food', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:47.803000', 'updated': '2023-11-01T18:59:47.803000', 'deleted': None}, {'id': 46, 'name': 'Chipotle', 'category': 'Fast Food', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:47.933000', 'updated': '2023-11-01T18:59:47.933000', 'deleted': None}]
    assert response.status_code == 200
    assert fastFood_rest_list == response.json()

def test_loadRestaurantsItalian():
    response = dailyTestClient.get("/loadRestaurants/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()

###################################################################
#USER REGISTRATION TESTING (Unit Testing)                                  
###################################################################

# Partition 1: Valid inputs that meet the criteria for credentials
def test_registration_clean(): #register with new email, username, and password (Parameters: email = brandNewEmail2@gmail.com, username = IAmFoodie2, password=SafePassword2)
    response = dailyTestClient.get("/registerTEST/brandNewEmail3@gmail.com/IAmFoodie3/SafePassword2")
    assert response.status_code == 200
    assert response.json() == {'success': 'true'} 

# Partition 2: Credentials for an existing account (ie. no sharing username or email with other accounts)
def test_registration_already_exists(): #register with existing username, email, password (Parameters: email = admin@email.com, username = admin, password=12345678longPassword)
    response = dailyTestClient.get("/registerTEST/admin@email.com/admin/12345678longPassword")
    assert response.status_code == 200
    assert response.json() == {'success': 'false', 'reason': 'Account with same username or email already exists'} 

# Partition 3: Password too short
def test_registration_too_short(): #register with password less than 8 characters (Parameters: email = anotherneew@email.com, username = neweUser, password=3)
    response = dailyTestClient.get("/registerTEST/anotherneew@email.com/neweUser/3")
    assert response.status_code == 200
    assert response.json() == {'success': 'false', 'reason': 'Password must be at least 8 characters long.'}


###################################################################
#WHITEBOX STATEMENT COVERAGE TESTING FOR payAndPlaceOrder                        
###################################################################

def test_placeOrderT1(): 
    response = dailyTestClient.get("/payAndPlaceOrder/2/44/12")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
def test_placeOrderT2(): 
    response = dailyTestClient.get("/payAndPlaceOrder/42000/42000/42000")
    assert response.status_code == 200
    assert response.json() == {"status": "unsuccessful"}
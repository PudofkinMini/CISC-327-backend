''' HEADER FOR FILE

THIS IS THE WHITE BOX TESTING SUITE FOR THE BACKEND OF OUR APPLICATION
IT WHITE BOX TESTS payAndPlaceOrder WITH STATEMENT COVERAGE TESTING, AND loadRestaurants WITH DECISION MUTATION COVERAGE TESTING
WE ARE USING TESTCLIENT FROM FASTAPI LIBRARY TO CONDUCT TEST API REQUESTS
WE ARE USING PYTEST TO DISPLAY AND ASSERT OUR TEST CASES
'''


#https://fastapi.tiangolo.com/tutorial/testing/
#pytest -r test_main.py -vv
#https://docs.pytest.org/en/6.2.x/usage.html Here is a list of available flags
from fastapi.testclient import TestClient
from unittest import TestCase
from .main import app

whiteBoxClient = TestClient(app)


###################################################################
#WHITEBOX STATEMENT COVERAGE TESTING FOR payAndPlaceOrder                        
###################################################################

def test_placeOrderT1(): 
    response = whiteBoxClient.get("/payAndPlaceOrder/2/44/12")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
def test_placeOrderT2(): 
    response = whiteBoxClient.get("/payAndPlaceOrder/42000/42000/42000")
    assert response.status_code == 200
    assert response.json() == {"status": "unsuccessful"}

###################################################################
#WHITEBOX STATEMENT MUTATION TESTING FOR loadRestaurants                        
###################################################################

def test_original_loadRestaurants():
    response = whiteBoxClient.get("/loadRestaurants/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()

def test_mutated_loadRestaurantsT1(): #MUTATED # 1
    response = whiteBoxClient.get("/mutatedLoadRestaurants1/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT2(): #MUTATED # 2
    response = whiteBoxClient.get("/mutatedLoadRestaurants2/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT3(): #MUTATED # 3
    response = whiteBoxClient.get("/mutatedLoadRestaurants3/Fast%20Food")
    fast_food_rest_list = [{"id": 44,"name": "McDonald's","category": "Fast Food","price": "$","logo": None,"created": "2023-11-01T18:59:47.673000","updated": "2023-11-01T18:59:47.673000","deleted": None},{"id": 45,"name": "Five Guys","category": "Fast Food","price": "$$","logo": None,"created": "2023-11-01T18:59:47.803000","updated": "2023-11-01T18:59:47.803000","deleted": None},{"id": 46,"name": "Chipotle","category": "Fast Food","price": "$$$","logo": None,"created": "2023-11-01T18:59:47.933000","updated": "2023-11-01T18:59:47.933000","deleted": None}]
    assert response.status_code == 200
    assert fast_food_rest_list == response.json()

def test_mutated_loadRestaurantsT4(): #MUTATED # 4
    response = whiteBoxClient.get("/mutatedLoadRestaurants4/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT5(): #MUTATED # 5
    response = whiteBoxClient.get("/mutatedLoadRestaurants5/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT6(): #MUTATED # 6
    response = whiteBoxClient.get("/mutatedLoadRestaurants6/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT7(): #MUTATED # 7
    response = whiteBoxClient.get("/mutatedLoadRestaurants7/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
    
def test_mutated_loadRestaurantsT8(): #MUTATED # 8
    response = whiteBoxClient.get("/mutatedLoadRestaurants8/Italian")
    italian_rest_list = [{'id': 56, 'name': 'GO', 'category': 'Italian', 'price': '$', 'logo': None, 'created': '2023-11-01T18:59:49.303000', 'updated': '2023-11-01T18:59:49.303000', 'deleted': None}, {'id': 57, 'name': 'Olivea', 'category': 'Italian', 'price': '$$', 'logo': None, 'created': '2023-11-01T18:59:49.450000', 'updated': '2023-11-01T18:59:49.450000', 'deleted': None}, {'id': 58, 'name': 'Casa Domenico', 'category': 'Italian', 'price': '$$$', 'logo': None, 'created': '2023-11-01T18:59:49.593000', 'updated': '2023-11-01T18:59:49.593000', 'deleted': None}]
    assert response.status_code == 200
    assert italian_rest_list == response.json()
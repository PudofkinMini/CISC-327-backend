'''
TODO:
    Login - in progress
    Create account - not started
    load restaurants - not started
    add/remove ordered_items - not started
    place order - not started
    view profile - not started
'''

from typing import Union
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.middleware.cors import CORSMiddleware
import logging
import pyodbc
import random

logging.basicConfig(level=logging.INFO)
pyodbc.drivers()

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:cisc-327-db.database.windows.net,1433;Database=cisc-327-db;Uid=group5;Pwd={Password1};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# Create a cursor from the connection


# Initialize webserver
app = FastAPI()

@app.get('/testSetup')
def tset():
    return {"msg": "Hello World"}
client = TestClient(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can also specify the exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# testable
@app.get("/register/{email}/{username}/{password}")
def register(email, username, password):
    if len(password) < 8:
        return {'success': 'false', 'reason': 'Password must be at least 8 characters long.'}
    cursor = cnxn.cursor()
    existing_accounts = cursor.execute(f"select * from accounts where username like '{username}' or email like '{email}'").fetchall()
    # print(existing_accounts)
    if len(existing_accounts) > 0:
        print("acc alr exists")
        return {'success': 'false', 'reason': 'Account with same username or email already exists'}
    query = cursor.execute(f"exec pi_create_account @email='{email}', @username='{username}', @password='{password}'")
    cnxn.commit()
    print(query)
    cursor.close()
    return {'success': 'true'}

# testable
@app.get("/login/{username}/{password}")
def login(username, password):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec ps_login @username='{username}', @password='{password}'").fetchone()
    print(query)
    if query:
        userid = query.id
        if userid:
            return {"userid": f"{userid}"}
    cursor.close()
    return {"userid": ""}

#testable
@app.get("/loadMenu/{restaurantid}")
def load_menu(restaurantid):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec ps_load_menu_items @restaurant_id='{restaurantid}'").fetchall()
    print(query)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    cursor.close()
    return results

#testable 
@app.get("/loadRestaurants/{category}")
def load_restaurants(category):
    cursor = cnxn.cursor()
    cat = category
    if category == 'Fast%20Food':
        cat = 'Fast Food'
    print(f"exec ps_load_restaurants @category='{cat}'")
    query = cursor.execute(f"exec ps_load_restaurants @category='{cat}'").fetchall()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    cursor.close()
    return results
    # return {"restaurants": }

# testable - unit testing
@app.get("/addToCart/{user_id}/{restaurant_id}/{menu_item_id}")
def load_restaurants(user_id, restaurant_id, menu_item_id):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec pi_add_menu_item_to_order @account_id={user_id}, @restaurant_id={restaurant_id}, @menu_item_id={menu_item_id}").fetchall()
    cnxn.commit()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    print('this is the data: ' + results)
    cursor.close()
    return results

# NOT testable
@app.get("/loadCart/{user_id}/{restaurant_id}")
def load_cart(user_id, restaurant_id):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec ps_load_cart @account_id={user_id}, @restaurant_id={restaurant_id}").fetchall()
    cnxn.commit()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    print(results)
    cursor.close()
    
    return results

# NOT testable
@app.get("/removeFromCart/{ordered_item_id}")
def load_cart(ordered_item_id):
    cursor = cnxn.cursor()
    cursor.execute(f"exec ps_remove_item_from_cart @ordered_item_id={ordered_item_id}")
    cnxn.commit()
    # columns = [column[0] for column in cursor.description]
    # results = [dict(zip(columns, row)) for row in query]
    # print(results)
    cursor.close()
    
    return {'status': 'success'}

# testable
@app.get("/payAndPlaceOrder/{user_id}/{restaurant_id}/{order_id}")
def load_cart(user_id, restaurant_id, order_id):
    cursor = cnxn.cursor()
    cursor.execute(f"exec pui_pay_and_place_order @account_id={user_id}, @restaurant_id={restaurant_id}, @order_id={order_id}")
    if cursor.rowcount == 0:
        return {'status': 'unsuccessful'}
    cnxn.commit()
    
    # columns = [column[0] for column in cursor.description]
    # results = [dict(zip(columns, row)) for row in query]
    # print(results)
    cursor.close()
    
    return {'status': 'success'}

@app.get("/loadOrders/{user_id}")
def load_orders(user_id):
    print(user_id)
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec ps_loadOrders @account_id={user_id}").fetchall()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    print(results)
    cursor.close()
    return results

@app.get("/confirmDelivery/{user_id}/{order_id}")
def load_orders(user_id, order_id):
    cursor = cnxn.cursor()
    cursor.execute(f"exec pui_confirm_order_delivery @account_id={user_id}, @order_id={order_id}")
    cnxn.commit()
    # columns = [column[0] for column in cursor.description]
    # results = [dict(zip(columns, row)) for row in query]
    # print(results)
    cursor.close()
    return {'success': 'true'}



    
    












































'''
@app.get("/generate")
def generate_data():
    
    
    # THIS IS FOR GENERATING DB DATA: RUN ONLY ONCE (ran it already)
    # Generating restaurants
    restaurants_categories = {
        'Fast Food': [("McDonald''s", '$'), ("Five Guys", '$$'), ('Chipotle', '$$$')],
        'Comfort': [("Pizza Hut", '$'), ("Lonestar", '$$'), ('Osmows', '$$$')], 
        'Chinese': [("Mandarin", '$'), ("VIP Chinese Restaurant", '$$'), ('Yellow River', '$$$')], 
        'Indian': [("Tasty Indian Bar & Grill", '$'), ("Namaste Kingston", '$$'), ('Flavours of India', '$$$')], 
        'Italian': [("GO", '$'), ("Olivea", '$$'), ('Casa Domenico', '$$$')], 
        'French': [("Geneva Crêpe Bistro", '$'), ("Chez Piggy", '$$'), ('Bistro Stefan', '$$$')], 
        'Vegetarian': [("Freshii", '$'), ("Atomica", '$$'), ('Copper Branch', '$$$')]
    }
    # Create insert statements for each restaurant
    for i in restaurants_categories:
        for j in restaurants_categories[i]:
            name = j[0]
            price = j[1]
            # sql_statement = f"exec pi_create_restaurant @name='{name}', @category='{i}', @price='{price}'"
            # try:
            #     cnxn.autocommit = False 
            #     cursor.execute(sql_statement)
            # except pyodbc.DatabaseError as err:
            #     cnxn.rollback()
            # else:
            #     cnxn.commit()
            # finally:
            #     cnxn.autocommit = True
                
            # print(sql_statement)
    
    # Generating restauraunt menus
    fast_foods = ['Grilled Chicken Sandwich', 'Fried Chicken Sandwich', 'Hamburger', 'Cheese Burger', 'Bacon Cheese Burger', 'Hot Dog', 'Fries', 'Soda Drink']
    comfort_foods = ['Pizza', 'Chicken Wings (8pc)', 'Chili', 'Ham & Cheese Sandwich', 'Mac & Cheese', 'Grilled Cheese', 'Fries', 'Soda Drink']
    chinese_foods = ['Peking Duck', 'Chow Mein', 'Mapo Tofu', 'Spring Rolls (3pc)', 'Wonton Soup', 'Chicken Fried Rice', 'Rice', 'Soda Drink', 'Tea']
    indian_foods = ['Coconut Tilapia Curry', 'Samosa (4pc)', 'Butter Chicken', 'Tandoori Chicken', 'Lamb Chops', 'Rice', 'Naan Bread', 'Soda Drink']
    italian_foods = ['Spaghetti Carbonara', 'Spaghetti Bolognese', 'Calamari', 'Bruschetta', 'Fettuccine Alfredo', 'Bread & Olive Oil', 'Soda Drink', 'Wine']
    french_foods = ['Escargot', 'Duck Confit', 'Steak Tartare', 'Steak Frites', 'Croissant', 'Foie Gras', 'Soda Drink', 'Wine']
    vegetarian_foods = ['Caesar Salad', 'Ranch Salad', 'Garden Salad', 'Green Goddess', 'Greek Salad', 'Egg Salad', 'Potatoe Salad', 'Fries', 'Soda Drink']
    categories = {
        'Fast Food': fast_foods,
        'Comfort': comfort_foods,
        'Chinese': chinese_foods,
        'Indian': indian_foods,
        'Italian': italian_foods,
        'French': french_foods,
        'Vegetarian': vegetarian_foods
    }
    
    id = 44
    for cat in restaurants_categories: # For every category
        for shop in restaurants_categories[cat]: # For every restaurant
            for food in categories[cat]: # For each food in that restaurant's category
                # Create a menu item with restaurant id, price
                name = food
                restaurant_id = id
                price = random.randint(10 + 5 * len(shop[1]), 10 + 15 * len(shop[1])) + 0.99
                calories = random.randint(500, 1000)
                sql_statement = f"exec pi_create_menu_item @name='{name}', @restaurant_id={restaurant_id}, @price={price}, @calories={calories}"
                try:
                    cnxn.autocommit = False 
                    cursor.execute(sql_statement)
                except pyodbc.DatabaseError as err:
                    cnxn.rollback()
                else:
                    cnxn.commit()
                finally:
                    cnxn.autocommit = True
                print(sql_statement)
            id += 1    
            
            
    
    return
'''


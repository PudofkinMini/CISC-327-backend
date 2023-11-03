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
from fastapi.middleware.cors import CORSMiddleware
import logging
import pyodbc
import random

logging.basicConfig(level=logging.INFO)
pyodbc.drivers()

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:cisc-327-db.database.windows.net,1433;Database=cisc-327-db;Uid=group5;Pwd={Password1};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;')

# Create a cursor from the connection


# Initialize webserver
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can also specify the exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/loadMenu/{restaurantid}")
def load_menu(restaurantid):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec ps_load_menu_items @restaurant_id='{restaurantid}'").fetchall()
    print(query)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    cursor.close()
    return results
    
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
    
@app.get("/addToCart/{user_id}/{restaurant_id}/{menu_item_id}")
def load_restaurants(user_id, restaurant_id, menu_item_id):
    cursor = cnxn.cursor()
    query = cursor.execute(f"exec pi_add_menu_item_to_order @account_id={user_id}, @restaurant_id={restaurant_id}, @menu_item_id={menu_item_id}").fetchall()
    cnxn.commit()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in query]
    print(results)
    cursor.close()
    
    return results

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

@app.get("/payAndPlaceOrder/{user_id}/{restaurant_id}/{order_id}")
def load_cart(user_id, restaurant_id, order_id):
    cursor = cnxn.cursor()
    cursor.execute(f"exec pui_pay_and_place_order @account_id={user_id}, @restaurant_id={restaurant_id}, @order_id={order_id}")
    cnxn.commit()
    # columns = [column[0] for column in cursor.description]
    # results = [dict(zip(columns, row)) for row in query]
    # print(results)
    cursor.close()
    
    return {'status': 'success'}
    
    












































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


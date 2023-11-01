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
import logging
import pyodbc
import random

logging.basicConfig(level=logging.INFO)
pyodbc.drivers()

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:cisc-327-db.database.windows.net,1433;Database=cisc-327-db;Uid=group5;Pwd={Password1};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;')

# Create a cursor from the connection
cursor = cnxn.cursor()

# Initialize webserver
app = FastAPI()

@app.get("/")
def read_root():
    print('something')
    print(cursor.execute('select * from accounts').fetchall())
    return {"Hello": "dude"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}












































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
    indian_foods = ['Coconut Tilapia Curry', 'Samosa (4pc)', 'Butter Chicken', 'Tandoori Chicken', 'LLamb Chops', 'Rice', 'Naan Bread', 'Soda Drink']
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


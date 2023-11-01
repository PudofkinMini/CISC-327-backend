from typing import Union
from fastapi import FastAPI
import pyodbc

pyodbc.drivers()
# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:cisc-327-db.database.windows.net,1433;Database=cisc-327-db;Uid=group5;Pwd={Password1};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;')

# Create a cursor from the connection
cursor = cnxn.cursor()

app = FastAPI()


@app.get("/")
def read_root():
    
    print(cursor.execute("select * from accounts").fetchall())
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

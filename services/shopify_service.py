from fastapi import FastAPI, HTTPException
import uvicorn
import requests
from database import get_mongodb
import os
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv('APIKEY')
SHOPIFY_STORE = os.getenv('STORE')
STORE_LOCATION_ID = os.getenv('STORE_LOCATIONID')
BASE_URL = f"https://{SHOPIFY_STORE}/admin/api/2024-04/"
headers = {'X-Shopify-Access-Token':API_KEY}
db = get_mongodb()

# Helper function to convert MongoDB ObjectId to string
def serialize_mongo_document(doc):
    if isinstance(doc, dict):
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc

async def get_orders():
    url = f"{BASE_URL}orders.json"
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        orders = res.json().get('orders',[])
        collection = db.Orders
        new_orders = []
        for order in orders:
            existing_order = collection.find_one({"id": order["id"]})
            if not existing_order:
                new_orders.append(order)

        if new_orders:
            collection.insert_many(new_orders)  
        saved_orders = list(collection.find())  
        serialized_orders = [serialize_mongo_document(order) for order in saved_orders]  # Serialize documents
        return {"message": "Orders fetched and stored in DB successfully.", "orders": serialized_orders}
    else:
        raise ValueError(f"Error in fetching order data \n status:{res.status_code}, message: {res.json()}")
    
async def get_products():
    url = f"{BASE_URL}products.json"
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        products = res.json().get('products',[])
        collection = db.Products
        new_products = []
        for product in products:
            existing_products = collection.find_one({"id": product["id"]})
            if not existing_products:
                new_products.append(product)

        if new_products:
            collection.insert_many(new_products)  
        saved_products = list(collection.find())  
        serialized_products = [serialize_mongo_document(product) for product in saved_products]  # Serialize documents
        return {"message": "Products fetched and stored in DB successfully.", "products": serialized_products}
        # return products
    else:
        raise ValueError(f"Error in fetching product data \n status:{res.status_code}, message: {res.json()}")
    
async def get_customers():
    url = f"{BASE_URL}customers.json"
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        customers = res.json().get('customers',[])
        collection = db.Customers
        new_customers = []
        for customer in customers:
            existing_customer = collection.find_one({"id": customer["id"]})
            if not existing_customer:
                new_customers.append(customer)

        if new_customers:
            collection.insert_many(new_customers)  
        saved_customers = list(collection.find())  
        serialized_customers = [serialize_mongo_document(customer) for customer in saved_customers]  # Serialize documents
        return {"message": "Customers fetched and stored in DB successfully.", "customers": serialized_customers}
    else:
        raise ValueError(f"Error in fetching customer data \n status:{res.status_code}, message: {res.json()}")
    
async def get_locations():
    url = f"{BASE_URL}locations.json"
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        locations = res.json().get('locations',[])
        collection = db.StoreLocations
        new_locations = []
        for location in locations:
            existing_locations = collection.find_one({"id": location["id"]})
            if not existing_locations:
                new_locations.append(location)
        if new_locations:
            collection.insert_many(new_locations)  
        saved_locations = list(collection.find())  
        serialized_locations = [serialize_mongo_document(location) for location in saved_locations]  # Serialize documents
        return {"message": "Locations fetched and stored in DB successfully.", "locations": serialized_locations}
    else:
        raise ValueError(f"Error in fetching location data \n status:{res.status_code}, message: {res.json()}")
    

async def get_inventory():
    url = f"{BASE_URL}inventory_levels.json?location_ids={STORE_LOCATION_ID}"
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        inventory_levels = res.json().get('inventory_levels',[])
        # db.InventoryLevels.insert_many()
        collection = db.InventoryLevels
        new_inventory = []
        for inventory in inventory_levels:
            existing_inventory = collection.find_one({"id": inventory["inventory_item_id"]})
            if not existing_inventory:
                new_inventory.append(inventory)

        if new_inventory:
            collection.insert_many(new_inventory)  
            
        saved_inventory= list(collection.find())  
        serialized_inventory = [serialize_mongo_document(inventory_data) for inventory_data in saved_inventory]  # Serialize documents
        return {"message": "inventory fetched and stored in DB successfully.", "Inventory": serialized_inventory}
    else:
        raise ValueError(f"Error in fetching location data \n status:{res.status_code}, message: {res.json()}")

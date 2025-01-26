from database import get_mongodb
from services import shopify_service
from fastapi import APIRouter

router = APIRouter()
db = get_mongodb()

@router.get("/shopify/get-orders")
async def fetch_orders():
    return await shopify_service.get_orders()

@router.get("/shopify/get-products")
async def fetch_products():
    return await shopify_service.get_products()

@router.get("/shopify/get-customers")
async def fetch_customers():
    return await shopify_service.get_customers()

@router.get("/shopify/get-inventory")
async def fetch_inventory():
    return await shopify_service.get_inventory()

@router.get("/shopify/get-locations")
async def fetch_store_location():
    return await shopify_service.get_locations()

from fastapi import FastAPI
import uvicorn
from controllers.shopify_controller import router

app =  FastAPI()
app.include_router(router=router, prefix="/api/v1", tags=["Shopify"])
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

    

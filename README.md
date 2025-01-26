# Shopify API Integration using FastAPI and Streamlit

This project integrates FastAPI APIs to fetch data from a Shopify store, stores it in MongoDB, and provides a Streamlit dashboard to visualize the orders based on some conditions and product details.
# Project Structure



Project Structure:
![image](https://github.com/user-attachments/assets/8beba282-ed84-4906-a3c8-9ad29428cfba)

# Features

## FastAPI APIs

Fetch Shopify orders and store Shopify order data in MongoDB.

## MongoDB

Use MongoDB for local data storage.

## Streamlit Dashboard

Visualize Shopify order and product data in a user-friendly dashboard.


## Prerequisites

Ensure you have the following installed:
- Python 3.9 or later
- MongoDB (running locally or on a server)
- Shopify store API credentials

---

## Installation and Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/saqiba123/shopify-app-using-fastapi.git
   cd shopify-app-using-fastapi

   ```

Create a Virtual Environment:
```
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```
Install Dependencies:
```
pip install -r requirements.txt
```
Set Up Environment Variables:
Create a .env file in the project root and add the following variables:
```
APIKEY=your_shopify_api_key
STORE_LOCATIONID=your_shopify_location_id
STORE=your_store_name
db_url=your_mongodb_connection_string
DB_NAME=your_db_name
```

# Running the Project

1. Start the MongoDB Server

Make sure your MongoDB server is running locally

2. Run the FastAPI Application

Navigate to the fastapi_app directory and start the FastAPI server:
```
uvicorn main:app --reload
```

Access the FastAPI application at:
```
http://localhost:8000
```
3. Run the Streamlit Dashboard

Navigate to the streamlit_dashboard directory and start the Streamlit application:
```
streamlit run streamlit_dashboard.py
```
Access the Streamlit dashboard at:
```
http://localhost:8501
```


![image](https://github.com/user-attachments/assets/00114dc4-156e-4da2-b68c-37cd29af8601)
![image](https://github.com/user-attachments/assets/85b28bbf-0bf1-4e53-9d6f-26a696ca300c)

![image](https://github.com/user-attachments/assets/56c7c7a6-f18f-4869-9cf3-a6810cb33f4f)
![image](https://github.com/user-attachments/assets/3f9d0fc9-2bbb-4ced-9631-2cfad035292a)

![image](https://github.com/user-attachments/assets/d74b3e2b-9ed8-4149-8119-3db776e949d2)
![image](https://github.com/user-attachments/assets/29dcb502-9059-478e-afb5-49639f136607)







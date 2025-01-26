# Shopify FastAPI and Streamlit Deployment

This project integrates FastAPI APIs to fetch data from a Shopify store, stores it in MongoDB, and provides a Streamlit dashboard to visualize the orders based on some conditions and products details.
# Project Structure
.
├── fastapi_app
│   ├── main.py                # Entry point for the FastAPI application
│   ├── database.py              # connecting with MongoDB
│   ├── controllers
|   |   └── __init__.py  
│   │   └── shopify_controller.py         # Shopify-related API endpoints
│   ├── services
|   |   └── __init__.py  
│   |   └── shopify_service.py  # Service logic for Shopify API integration
├── streamlit_dashboard.py # Streamlit app for data visualization
├── requirements.txt           # Python dependencies

# Features

## FastAPI APIs

Fetch Shopify orders with "fulfilled" status.

Store Shopify order data in MongoDB.

## MongoDB

Use MongoDB for local data storage.

## Streamlit Dashboard

Visualize Shopify order and product data in a user-friendly dashboard.


# Running the Project

1. Start the MongoDB Server

Make sure your MongoDB server is running locally

2. Run the FastAPI Application

Navigate to the fastapi_app directory and start the FastAPI server:

uvicorn main:app --reload

Access the FastAPI application at:

http://localhost:8000

3. Run the Streamlit Dashboard

Navigate to the streamlit_dashboard directory and start the Streamlit application:

streamlit run streamlit_dashboard.py

Access the Streamlit dashboard at:

http://localhost:8501



![image](https://github.com/user-attachments/assets/00114dc4-156e-4da2-b68c-37cd29af8601)
![image](https://github.com/user-attachments/assets/85b28bbf-0bf1-4e53-9d6f-26a696ca300c)

![image](https://github.com/user-attachments/assets/56c7c7a6-f18f-4869-9cf3-a6810cb33f4f)
![image](https://github.com/user-attachments/assets/3f9d0fc9-2bbb-4ced-9631-2cfad035292a)

![image](https://github.com/user-attachments/assets/d74b3e2b-9ed8-4149-8119-3db776e949d2)
![image](https://github.com/user-attachments/assets/29dcb502-9059-478e-afb5-49639f136607)







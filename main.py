from fastapi import FastAPI
from routes import product

app = FastAPI(title="Ecommerce API", version="1.0")

app.include_router(product.router)


@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce API"}

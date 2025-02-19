from fastapi import FastAPI
from routes import product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ecommerce API", version="1.0")

app.include_router(product.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ En producción, limita esto a los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce API"}

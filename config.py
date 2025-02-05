import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://root@localhost:3306/ecommerce_db"
)

print(f"Conectando a: {DATABASE_URL}")  # Para depuración

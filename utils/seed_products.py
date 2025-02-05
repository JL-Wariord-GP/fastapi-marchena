from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models.product import Product
import random

# Crear una sesión de la base de datos
db: Session = SessionLocal()

# Lista de productos de ejemplo
products = [
    {
        "name": "Laptop Dell XPS 13",
        "description": "Laptop ultradelgada con pantalla 4K",
        "price": 1299.99,
        "stock": 10,
    },
    {
        "name": "iPhone 14 Pro",
        "description": "Smartphone Apple con chip A16 Bionic",
        "price": 999.99,
        "stock": 20,
    },
    {
        "name": "Samsung Galaxy S23",
        "description": "Teléfono Samsung con pantalla AMOLED",
        "price": 899.99,
        "stock": 15,
    },
    {
        "name": "Teclado Mecánico RGB",
        "description": "Teclado gamer con switches Cherry MX",
        "price": 79.99,
        "stock": 50,
    },
    {
        "name": "Monitor 27'' 144Hz",
        "description": "Monitor para gaming con alta tasa de refresco",
        "price": 299.99,
        "stock": 30,
    },
    {
        "name": "Silla Gamer",
        "description": "Silla ergonómica con soporte lumbar",
        "price": 199.99,
        "stock": 25,
    },
    {
        "name": "SSD NVMe 1TB",
        "description": "Disco sólido M.2 para alto rendimiento",
        "price": 129.99,
        "stock": 40,
    },
    {
        "name": "Tarjeta Gráfica RTX 4090",
        "description": "GPU potente para gaming y diseño",
        "price": 1599.99,
        "stock": 5,
    },
    {
        "name": "Mouse Inalámbrico Logitech",
        "description": "Mouse ergonómico con batería de larga duración",
        "price": 49.99,
        "stock": 60,
    },
    {
        "name": "Auriculares Inalámbricos Sony",
        "description": "Auriculares con cancelación de ruido",
        "price": 199.99,
        "stock": 35,
    },
]

# Insertar 50 productos variando los datos
for i in range(50):
    product_data = random.choice(products)  # Selecciona un producto de la lista
    new_product = Product(
        name=f"{product_data['name']} - Modelo {i+1}",
        description=product_data["description"],
        price=round(
            product_data["price"] * (1 + random.uniform(-0.2, 0.2)), 2
        ),  # Variar el precio en un 20%
        stock=random.randint(5, 100),  # Stock aleatorio entre 5 y 100
    )
    db.add(new_product)

# Guardar cambios en la base de datos
db.commit()

print("✅ Se insertaron 50 productos en la base de datos.")

# Cerrar la sesión
db.close()

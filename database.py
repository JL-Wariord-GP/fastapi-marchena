from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from db_base import Base  # Importa Base desde db_base.py

# Importa modelos antes de crear las tablas
import models.user
import models.product
import models.order
import models.invoice

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Crea todas las tablas en MySQL."""
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas en MySQL")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    init_db()

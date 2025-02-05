from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from db_base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total = Column(Float, nullable=False)

    user = relationship("User", back_populates="orders")
    invoice = relationship("Invoice", uselist=False, back_populates="order")

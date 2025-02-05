from pydantic import BaseModel
from typing import List


class OrderBase(BaseModel):
    user_id: int
    total: float


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True

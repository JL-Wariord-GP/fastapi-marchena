from pydantic import BaseModel
from datetime import datetime


class InvoiceBase(BaseModel):
    order_id: int


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

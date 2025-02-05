from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.invoice_service import create_invoice, get_invoice
from schemas.invoice import InvoiceCreate, InvoiceResponse

router = APIRouter(prefix="/invoices", tags=["Invoices"])


@router.post("/", response_model=InvoiceResponse)
def create_new_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice_by_id(invoice_id: int, db: Session = Depends(get_db)):
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

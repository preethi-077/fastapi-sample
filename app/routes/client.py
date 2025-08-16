from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import client as client_service
from app.schemas.client import ClientCreate, ClientResponse, ClientUpdate


router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_service.create_client(db, client)

@router.get("/", response_model=list[ClientResponse])
def read_clients(db: Session = Depends(get_db)):
    return client_service.get_clients(db)

@router.get("/{client_id}", response_model=ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = client_service.get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientResponse)
def update_client(client_id: int, client_data: ClientUpdate, db: Session = Depends(get_db)):
    client = client_service.update_client(db, client_id, client_data)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = client_service.delete_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}

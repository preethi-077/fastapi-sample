from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas.client import ClientCreate, ClientResponse, ClientUpdate

def create_client(db: Session, client: ClientCreate):
    db_client = models.client.Client(
        name=client.name,
        email=client.email,
        client_type=client.client_type,
        phone=client.phone,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session):
    return db.query(models.client.Client).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(models.client.Client).filter(models.client.Client.id == client_id).first()

def update_client(db: Session, client_id: int, client_data: ClientUpdate):
    db_client = get_client_by_id(db, client_id)
    if not db_client:
        return None
    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client_by_id(db, client_id)
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client

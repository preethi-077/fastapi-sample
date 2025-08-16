import enum
from sqlalchemy import Column, Integer, String, Enum
from app.db.database import Base

# Define Enum for client_type
class ClientTypeEnum(str, enum.Enum):
    RETAIL = "Retail"
    CORPORATE = "Corporate"


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    client_type = Column(Enum(ClientTypeEnum),index=True, nullable=False)
    phone = Column(String, nullable=False)
    


from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from database.database import Base # Importas la Base que creaste
from sqlalchemy.orm import relationship

class Role(Base):
    # Nombre de la tabla en tu base de datos (Postgres/SQLite)
    __tablename__ = "role" 

    # Definición de las columnas basándonos en tu código
    role_pk = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, unique=True, index=True)
    role_description = Column(String)
    is_active = Column(Boolean, default=True)  
    
    #Relationships
    relationships = {"users": relationship("User", back_populates="role")}
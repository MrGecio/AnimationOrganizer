from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database.database import Base # Importas la Base que creaste
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    # Nombre de la tabla en tu base de datos (Postgres/SQLite)
    __tablename__ = "user" 

    # Definición de las columnas basándonos en tu código
    user_pk = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_email = Column(String, unique=True, index=True)
    user_password = Column(String)
    user_status = Column(String)  
    user_created_at = Column(Date) 
    user_updated_at = Column(Date)  
    
 
    
    #Foreign Keys
    role_pk = Column(Integer, ForeignKey("role.role_pk")) 
    
    #Relationships
    role = relationship("Role", back_populates="users")
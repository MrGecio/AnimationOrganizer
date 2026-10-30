from sqlalchemy import Column, Integer, String, Date, ForeignKey,Boolean
from database.database import Base # Importas la Base que creaste
from sqlalchemy.orm import relationship
from datetime import datetime

class Views(Base):
    # Nombre de la tabla en tu base de datos (Postgres/SQLite)
    __tablename__ = "views" 

    # Definición de las columnas basándonos en tu código
    views_pk = Column(Integer, primary_key=True, index=True)
    views_name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    
 
    
    #Foreign Keys
    groups_tasks_views_pk = Column(Integer, ForeignKey("groups_tasks_views.groups_tasks_views_pk"))

    #Relationships
    groups_tasks_views = relationship("GroupsTasksViews", back_populates="views")
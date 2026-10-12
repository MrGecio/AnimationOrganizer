#FastApi
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

#Middleware
from fastapi.middleware.cors import CORSMiddleware



#Routers


#Users
from routers.login_router import router as login_router


#main
app = FastAPI()

#middleware
#Rutas del frontend que se permiten para hacer peticiones al backend
origins = [
    "http://localhost:3000",
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],       #Permitir los metodos HTTP si quiero bloquear algun metodo hay que editar aqui
    allow_headers=["*"],       # Permite todos los headers
)

#Invocaione de los Routers
# app.include_router(type_router)




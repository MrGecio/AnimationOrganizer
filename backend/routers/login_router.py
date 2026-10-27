
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List

from model.user import User
from model.rol import Role

from sqlalchemy.orm import Session
from database.database import SessionLocal, engine

router = APIRouter()


class LoginRequest(BaseModel):
    user_name: str
    user_password: str


class UserClass(BaseModel):
    user_pk: int
    user_name: str
    user_email: str
    user_password: str
    role_pk: int


# Conexion a la base de datos
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")

async def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.user_name == login_data.user_name).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if usuario.user_password != login_data.user_password:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return {
        "mensaje": "Login exitoso",
        "user": {
            "user_pk": usuario.user_pk,
            "user_name": usuario.user_name,
            "user_email": usuario.user_email,
            "role_pk": usuario.role_pk,
        },
    }


### Endpoints
# GET
@router.get("/user")
async def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = (
        db.query(
            User.user_pk,
            User.user_name,
            User.user_email,
            Role.role_name,
        )
        .join(Role, User.role_pk == Role.role_pk)
        .all()
    )

    datos_formateados = []
    for fila in usuarios:
        datos_formateados.append(
            {
                "user_pk": fila.user_pk,
                "user_name": fila.user_name,
                "user_email": fila.user_email,
                "role_name": fila.role_name,
            }
        )

    return {
        "mensaje": "Conexión a la base de datos exitosa",
        "total_users": len(datos_formateados),
        "data": datos_formateados,
    }


#POST
@router.post("/user")
async def crear_usuario(user_data: UserClass, db: Session = Depends(get_db)):
    nuevo_usuario = User(
        user_pk=user_data.user_pk,
        user_name=user_data.user_name,
        user_email=user_data.user_email,
        user_password=user_data.user_password,
        role_pk=user_data.role_pk,
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario creado", "Usuario": nuevo_usuario}


#POST BULK
@router.post("/user/bulk")
async def crear_multiples_usuarios(usuarios_data: List[UserClass], db: Session = Depends(get_db)):
    nuevos_usuarios = [
        User(
            user_pk=item.user_pk,
            user_name=item.user_name,
            user_email=item.user_email,
            user_password=item.user_password,
            role_pk=item.role_pk,
        )
        for item in usuarios_data
    ]

    db.add_all(nuevos_usuarios)
    db.commit()

    return {"mensaje": f"Se insertaron {len(nuevos_usuarios)} registros de usuarios"}


#PUT
@router.put(
    "/user/{user_pk}",
    responses={404: {"description": "Usuario no encontrado"}},
)
async def actualizar_usuario(user_pk: int, user_data: UserClass, db: Session = Depends(get_db)):
    usuario_actual = db.query(User).filter(User.user_pk == user_pk).first()

    if not usuario_actual:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario_actual.user_pk = user_data.user_pk
    usuario_actual.user_name = user_data.user_name
    usuario_actual.user_email = user_data.user_email
    usuario_actual.user_password = user_data.user_password
    usuario_actual.role_pk = user_data.role_pk

    db.commit()
    db.refresh(usuario_actual)

    return {"mensaje": "Usuario actualizado", "Usuario": usuario_actual}


# DELETE
@router.delete(
    "/user/{user_pk}",
    responses={404: {"description": "Usuario no encontrado"}},
)
async def borrar_usuario(user_pk: int, db: Session = Depends(get_db)):
    usuario_actual = db.query(User).filter(User.user_pk == user_pk).first()

    if not usuario_actual:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario_actual)
    db.commit()

    return {"mensaje": f"Usuario con ID {user_pk} borrado correctamente"}
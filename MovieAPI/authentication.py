from fastapi import *
from schemas import *
from models import *
from database import *

authentication = APIRouter()


@authentication.post('/login')
async def login(email: User, password: User):
    email = users_serializer(user_list.find({"email": email}))
    password = users_serializer(user_list.find({"password": password}))
    if not email & password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user credentials')
    return {"status": "ok", "details": f"Welcome! {User.name} "}

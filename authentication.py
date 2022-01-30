from fastapi import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database import user_list
from models import User
from schemas import users_serializer

authentication = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@authentication.post('/token')
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + "'s token", "access_type": "bearer"}


@authentication.post('/login')
async def login(form_email: OAuth2PasswordRequestForm = Depends(oauth2_scheme),
                form_password: OAuth2PasswordRequestForm = Depends(oauth2_scheme)):
    email = users_serializer(user_list.find_one({"email": User.email}))
    password = users_serializer(user_list.find_one({"password": User.password}))
    if not email == form_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user email')
    if not password == form_password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user password')
    return {"status": "ok", "details": f"Welcome! {User.name} "}

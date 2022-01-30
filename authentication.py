from fastapi import *
from schemas import *
from models import *
from database import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


authentication = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@authentication.post('/token')
async def user_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + "token"}


@authentication.post('/login')
async def login(email: OAuth2PasswordRequestForm = Depends(oauth2_scheme),
                password:  OAuth2PasswordRequestForm = Depends(oauth2_scheme)):
    email = users_serializer(user_list.find_one({"email": email.username}))
    password = users_serializer(user_list.find_one({"password": password.password}))
    if not email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user email')
    if not password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user password')
    return {"status": "ok", "details": f"Welcome! {User.name} "}

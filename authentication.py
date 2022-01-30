from fastapi import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

authentication = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

email = "rohit@gmail.com"
password = "admin123"


@authentication.post('/login')
async def login(form_email: OAuth2PasswordRequestForm = Depends(),
                form_password: OAuth2PasswordRequestForm = Depends()):
    if form_email.username != email :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user email')
    if form_password.password != password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect user password')
    return {"status": "ok", "details": f"Welcome! {form_email.username} "}

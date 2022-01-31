from fastapi import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

authentication = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


email = "rohit@gmail.com"
password = "admin123"


@authentication.post('/login')
async def login(form_email: OAuth2PasswordRequestForm = Depends(),
                form_password: OAuth2PasswordRequestForm = Depends()):
    if form_email.username == email:
        if form_password.password == password:
            return {"status": "ok", "details": f"Welcome! {form_email.username} "}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect email or password')

# login logic

# @authentication.post('/login')
# async def login(form_email: OAuth2PasswordRequestForm = Depends(),
#                form_password: OAuth2PasswordRequestForm = Depends()):
#    email = users_serializer(user_list.find_one({"email": form_email.username}))
#    password = users_serializer(user_list.find_one({"password": form_password.password}))
#    print(email)
#    print(password)
#    if form_email.username == email:
#        if form_password.password == password:
#            return {"status": "ok", "details": f"Welcome! {form_email.username} "}
#    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect email or password')

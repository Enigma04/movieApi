from fastapi import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

authentication = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@authentication.post('/token')
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + "'s token", "access_type": "bearer"}
from bson import ObjectId
from fastapi import *
from database import user_list
from models import User
from schemas import users_serializer
import authentication


users_router = APIRouter()


@users_router.get('/users', tags=['user'])
async def get_all_users():
    users = users_serializer(user_list.find())
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No users found')
    return {'status': 'ok', 'data': users}


@users_router.get('/users/{id}', tags=['user'])
async def get_user(uid: str, token: str = Depends(authentication.oauth2_scheme)):
    print(token)
    user = users_serializer(user_list.find({"_id": ObjectId(uid)}))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
    return {'status': 'ok', 'data': user}


@users_router.post('/users', tags=['user'])
async def create_user(user: User, token: str = Depends(authentication.oauth2_scheme)):
    _id = user_list.insert_one(dict(user))
    add_user = users_serializer(user_list.find({"_id": _id.inserted_id}))
    return {'status': 'ok', 'data': add_user}


@users_router.delete('/users/{id}', tags=['user'])
async def delete_user(uid: str, token: str = Depends(authentication.oauth2_scheme)):
    user = user_list.find_one_and_delete({"_id": ObjectId(uid)})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
    return {'status': 'ok', 'data': "user is deleted"}

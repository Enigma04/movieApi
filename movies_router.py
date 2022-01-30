from fastapi import *

import authentication
from schemas import *
from database import *
from models import Movie

movie_router = APIRouter()


# get
@movie_router.get('/all_movies', tags=['movies'])
async def get_movies():
    movie = movies_serializer(movie_list.find())
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No movies found')
    return {'status': 'ok', 'data': movie}


@movie_router.get('/movies/{name}', tags=['movies'])
async def get_movie(movie_name: str, token: str = Depends(authentication.oauth2_scheme)):
    movie = movies_serializer(movie_list.find({"title": movie_name}))
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No movies found')
    return {'status': 'ok', 'user': token, 'data': movie}


@movie_router.post('/all_movies', tags=['movies'])
async def create_movie(movie: Movie, token: str = Depends(authentication.oauth2_scheme)):
    _id = movie_list.insert_one(dict(movie))
    movie = movies_serializer(movie_list.find({"_id": _id.inserted_id}))
    return {'status': 'ok', 'user': token, 'data': movie}


@movie_router.delete('/movies/{name}', tags=['movies'])
async def delete_movie(movie_name: str, token: str = Depends(authentication.oauth2_scheme)):
    movie = movie_list.find_one_and_delete({"title": movie_name})
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No movie with name {movie_name} found')
    return {'status': 'ok', 'user': token, 'data': f"movie {movie_name} is deleted"}

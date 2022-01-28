from fastapi import *
from schemas import *
from database import *


movie_router = APIRouter()


# get
@movie_router.get('/all_movies', tags=['movies'])
async def get_movies():
    movie = movies_serializer(movie_list.find())
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No movies found')
    return {'status': 'ok', 'data': movie}


@movie_router.get('/movies/{name}', tags=['movies'])
async def get_movie(movie_name: str):
    movie = movies_serializer(movie_list.find({"title": movie_name}))
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No movies found')
    return {'status': 'ok', 'data': movie}


# post
@movie_router.post('/all_movies', tags=['movies'])
async def create_movie(movie: Movies):
    _id = movie_list.insert_one(dict(movie))
    movie = movies_serializer(movie_list.find({"_id": _id.inserted_id}))
    return {'status': 'ok', 'data': movie}


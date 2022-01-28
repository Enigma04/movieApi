from movies_router import *
from users_routers import *
from authentication import *

app = FastAPI()

app.include_router(movie_router)
app.include_router(users_router)
app.include_router(authentication)

 
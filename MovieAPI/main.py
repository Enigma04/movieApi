from fastapi import *

app = FastAPI()


@app.get('/')
def test():
    return "hello"
 
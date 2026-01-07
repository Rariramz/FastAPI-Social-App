from fastapi import FastAPI
from app.routers import posts_router


app = FastAPI(title="Social App API")

app.include_router(posts_router)

@app.get('/healthcheck')
def healthcheck():
    return {'status': 'ok'}

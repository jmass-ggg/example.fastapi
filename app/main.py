from fastapi import FastAPI
from app.api import user_routes
from app.deps import Base,engine
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins = ["https://www.google.com","https://www.youtube.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(user_routes.router)

@app.get('/')
def hello():
    return {'hello':'world'}
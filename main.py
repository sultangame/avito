from fastapi.middleware.cors import CORSMiddleware
from src.main_api import api
from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="shop application",
)
app.include_router(api)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:4000",
    "http://localhost:5000",
    "http://localhost:6000",
    "http://localhost:7000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=4000)

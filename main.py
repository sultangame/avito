from src.main_api import api
from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="shop application",
)
app.include_router(api)

@app.get("/")
async def root():
    return {"Message": "Hello world"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=4000)

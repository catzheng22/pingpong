from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping", status_code=201)
async def ping():
    return {"message": "pong"}
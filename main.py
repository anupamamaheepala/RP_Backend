from fastapi import FastAPI
from routes import data  # Ensure this matches your route file name

app = FastAPI()

app.include_router(data.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RP Backend!"}
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from routes import data

# app = FastAPI()

# # CORS middleware to allow requests from Flutter app
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(data.router)

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to RP Backend!"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import data

app = FastAPI()

# CORS middleware to allow requests from Flutter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - you can specify domains later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RP Backend!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FastAPI Backend"}
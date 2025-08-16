# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def basic():
#     return {"message": "Hello preethi"}
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.routes import client as client_router


# Create tables on startup (simple dev-friendly approach)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + PostgreSQL", version="0.1.0")

# CORS (open for dev; tighten in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers if they exist
# try:
#     app.include_router(client_router.router)
# except Exception:
#     pass
app.include_router(client_router.router)


@app.get("/")
def root():
    return {"message": "API is running "}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import documents, verification
from .database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Legal Document Verification API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(documents.router)
app.include_router(verification.router)

@app.get("/")
def read_root():
    return {"message": "Legal Document Verification API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

from fastapi import FastAPI

app = FastAPI(
    title="DevOps Automation Platform",
    description="API-driven DevOps automation project",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "DevOps Automation Platform is running!"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "DevOps Automation Platform"
    }

@app.get("/api/v1/status")
def application_status():
    return {
        "status": "running",
        "version": "1.0.0"
    }
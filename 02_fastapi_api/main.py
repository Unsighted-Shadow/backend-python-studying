from fastapi import FastAPI

app = FastAPI()

@app.get("/api/status")
def server_status():
    
    return {
        "server": "FastAPI",
        "status": "active",
        "message": "Welcome to my FastAPI Portfolio API!"   
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Next.js frontend
    "http://127.0.0.1:3000", # Next.js frontend
    # Add any other origins if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
async def read_root():
    return {"message": "Welcome to the API"}

@app.get("/api/greetings")
async def get_greetings():
    # Temporarily returning a static list as 'ai' package is problematic
    return {"greetings": ["Hello from FastAPI (static)!", "Hola (static)!", "Bonjour (static)!"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

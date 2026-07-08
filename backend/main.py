from fastapi import FastAPI

app = FastAPI(
    title="CodeMentor AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CodeMentor AI!"
    }
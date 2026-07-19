from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FlyRank!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/test-post")
async def test_post(msg):
    return {"message": msg}

@app.get("/test-get")
async def test_get():
    return {"message": "test get"}

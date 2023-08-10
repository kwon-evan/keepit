from fastapi import FastAPI
from keepit.user import user

app = FastAPI()

app.include_router(user)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/test-post")
async def test_post(msg):
    return {"message": msg}


@app.get("/test-get")
async def test_get():
    return {"message": "test get"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

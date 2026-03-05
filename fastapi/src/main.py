from web.creature import router as creature_router
from web.explorer import router as explorer_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(explorer_router)
app.include_router(creature_router)


@app.get("/")
def top():
    return "top here"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)

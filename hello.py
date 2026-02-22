from fastapi import Body, FastAPI, Header

app = FastAPI()
@app.post("/hi")
def greet(name: str = Header()):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}

@app.post("/agent")
def agent(user_agent: str = Header()):
    return {"message": f"Hello, {user_agent}! This is an agent endpoint."}
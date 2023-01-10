from fastapi import FastAPI
import consumidor_CRUD as consumidor_CRUD

app = FastAPI()



@app.get("/")
async def Home():
    return "Home"


app.include_router(consumidor_CRUD.router)


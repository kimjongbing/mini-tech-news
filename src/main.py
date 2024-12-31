from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/")
async def root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, "static", "index.html")

    with open(index_path) as f:
        return HTMLResponse(content=f.read())


from .api.hackernews import router

app.include_router(router)

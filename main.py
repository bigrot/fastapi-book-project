from fastapi import FastAPI

from api.router import api_router

app = FastAPI()


app.include_router(api_router)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

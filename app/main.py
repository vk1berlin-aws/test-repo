from fastapi import FastAPI

from app.utils import format_response

app = FastAPI(title="Sample FastAPI Service", version="0.1.0")


@app.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Retrieve a user by their ID.

    TODO: Add input validation for user_id
    """
    # TODO: Add input validation for user_id
    # For now, just return a placeholder without checking if the user exists
    user_data = {
        "id": user_id,
        "name": "placeholder",
        "email": "placeholder@example.com",
    }
    return format_response(user_data)

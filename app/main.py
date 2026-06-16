from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.utils import format_response

app = FastAPI(title="User Service API", version="1.0.0")


MOCK_USERS = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
}


@app.get("/health")
def health_check():
    """Return service health status."""
    return {"status": "healthy"}


@app.get("/users/{user_id}")
def get_user(user_id: str):
    """Retrieve a user by ID.

    Validates that user_id is a positive integer and returns the
    corresponding user or a 404 if not found.
    """
    try:
        uid = int(user_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=422,
            detail=f"Invalid user_id: '{user_id}'. Must be a positive integer.",
        )

    if uid <= 0:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid user_id: '{user_id}'. Must be a positive integer.",
        )

    user = MOCK_USERS.get(uid)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {uid} not found.")

    return format_response(data=user, message="User retrieved successfully")

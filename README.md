# User Service API

A lightweight FastAPI service that provides user lookup functionality with input validation and a standard response envelope.

## Prerequisites

- Python 3.10+

## Setup

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application** (optional):

   Copy or edit `config.yaml` in the project root to customise settings:

   ```yaml
   app_name: user-service
   debug: false
   port: 8000
   ```

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs are served at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Path              | Description            |
|--------|-------------------|------------------------|
| GET    | `/health`         | Service health check   |
| GET    | `/users/{user_id}`| Retrieve a user by ID  |

## Running Tests

```bash
pytest
```

To run with verbose output and coverage:

```bash
pytest -v --tb=short
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and route handlers
│   └── utils.py         # Utility functions (response formatting, config parsing)
├── tests/
│   ├── __init__.py
│   └── test_placeholder.py  # Unit tests
├── config.yaml          # Application configuration
├── requirements.txt     # Python dependencies
└── README.md
```

## Authors

- Vikram

# Todo Reminder API

A high-quality RESTful API for managing todo reminders, built with FastAPI and MongoDB (motor).

## Features
- Create, list, and mark todos as done
- Overdue reminders via background task
- Modular routers, controllers, and middleware
- JWT authentication (optional, see below)
- Request logging middleware

## Requirements
- Python 3.9+
- MongoDB (local or remote)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables as needed (optional):
   - `MONGODB_URL` (default: mongodb://localhost:27017)
   - `MONGO_DB_NAME` (default: todo_db)
3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints
- `POST /todos` – Create a todo
- `GET /todos` – List todos (add `?overdue=true` to filter overdue)
- `PATCH /todos/{todo_id}` – Mark as done

## Project Structure
- `main.py` – App entrypoint
- `config/` – Database config
- `models/` – Pydantic models
- `controllers/` – Business logic
- `routers/` – API routes
- `middleware/` – Custom middleware

## Notes
- The background task logs overdue todos every 24h (adjustable for testing).


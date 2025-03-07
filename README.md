# Backend - Django Todo App

This is the backend API for a simple Todo application built using Django. The API handles tasks including fetching, adding, updating, and deleting tasks. It is connected to a SQLite database.

## Prerequisites

- Python 3.12+ (ensure you have Python installed)
- Django 5.1.6
- Django REST Framework
- CORS Headers

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/backend-todo-app.git
   cd backend-todo-app
   ```
2. **Create a virtual environment**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
    pip install -r requirements.txt
   ```
4. **Configure CORS (allow requests from your frontend): Make sure to configure CORS settings in settings.py**:

   ```bash
    CORS_ALLOW_ALL_ORIGINS = True
   ```

5. **Run migrations:**:
   ```bash
    python manage.py migrate
   ```
6. **Create a superuser (optional, for admin access)**:
   ```bash
    python manage.py createsuperuser
   ```
7. **Start the Server**:
   ```bash
    python manage.py runserver
   ```

## API Endpoints

### `GET /task/`

- **Description**: Fetches all tasks from the database.

### `POST /task/`

- **Description**: Adds a new task.
- **Request Body**:
  ```json
  {
    "title": "Task Title"
  }
  ```

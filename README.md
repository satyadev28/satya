# Todo List API with FastAPI

## Description
This is a simple RESTful API for managing a todo list using FastAPI. The API supports CRUD operations and uses in-memory storage for todo items.

## Features
- Create a todo item
- Read all todo items with pagination
- Read a single todo item
- Update a todo item
- Delete a todo item
- Basic authentication

## Setup

### Requirements
- Python 3.7+
- FastAPI
- Uvicorn

### Installation
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd todo_list_api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

## Usage
Once the application is running, you can use an API client like Postman or curl to interact with the API.

### Endpoints

- *Create a Todo Item*
    ```bash
    POST /todos/
    {
        "title": "Example Todo",
        "description": "This is an example todo"
    }
    ```

- *Read All Todo Items*
    ```bash
    GET /todos/
    ```

- *Read a Single Todo Item*
    ```bash
    GET /todos/{todo_id}
    ```

- *Update a Todo Item*
    ```bash
    PUT /todos/{todo_id}
    {
        "title": "Updated Todo",
        "description": "This is an updated description",
        "completed": true
    }
    ```

- *Delete a Todo Item*
    ```bash
    DELETE /todos/{todo_id}
    ```

## Authentication
The API uses basic authentication. Use the following credentials:

- **Username:** admin
- **Password:** password

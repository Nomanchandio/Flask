# Flask Todo Application

## Description
A simple Flask application providing CRUD operations for a Todo list using SQLite as the database.

## Setup

### Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd flask-todo-app
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    # On Windows
    venv\Scripts\activate
    # On Unix or MacOS
    source venv/bin/activate
    ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup
1. Initialize the database:
    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

### Running the Application
1. Start the Flask application:
    ```bash
    flask run
    ```
2. The application will be accessible at `http://127.0.0.1:5001`.

### API Endpoints

- **POST /**: Create a new todo item.
- **GET /**: Read all todo items.
- **POST /create**: Create a new todo item (API).
- **GET /read**: Read all todo items (API).
- **PUT /update/<int:sno>**: Update a specific todo item.
- **DELETE /delete/<int:sno>**: Delete a specific todo item.

### License
MIT License

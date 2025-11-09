# FastAPI CRUD Example – Shapes API

This project is a simple FastAPI application that demonstrates basic **CRUD (Create, Read, Update, Delete)** operations for managing geometric shapes.

> **Note:** This project was inspired by a [Real Python](https://realpython.com/courses/python-rest-apis-with-fastapi/) tutorial on FastAPI.  
> I updated and added commentary to parts of the original example to explain CRUD operations and API design patterns.  
> This repository is for **educational purposes only**.

---

## Features

- **GET** `/shapes` — Retrieve all shapes  
- **GET** `/shapes/{shape_id}` — Retrieve a shape by ID  
- **POST** `/shapes` — Add a new shape  
- **PUT** `/shapes/{shape_id}` — Update a shape  
- **DELETE** `/shapes/{shape_id}` — Delete a shape  

All responses are returned in JSON.

---

## Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/HogRed/python_fastapi.git
   cd python_fastapi

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the FastAPI app**
    ```bash
    uvicorn main:app --host "0.0.0.0" --port 8000 --reload

5. **Access the API**

Root endpoint: http://localhost:8000/shapes

## Example Request

**POST /shapes**

**Response**

{
  "message": "Shape with id 3 created successfully"
}
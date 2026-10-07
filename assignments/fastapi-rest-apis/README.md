# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API in Python using FastAPI and learn how to define routes, handle JSON requests, and return structured responses.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application and create a basic API endpoint that returns a list of sample items or a simple welcome message.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Create at least one GET endpoint that returns JSON data
- Use a simple in-memory data structure such as a list or dictionary
- Run the app locally with an appropriate command

### 🛠️ Add CRUD-style Endpoints

#### Description
Extend the app by adding endpoints to create, read, and update data for a simple resource such as tasks, books, or students.

#### Requirements
Completed program should:

- Create a POST endpoint that accepts JSON input
- Return the created item with a success response
- Add a GET endpoint to fetch all items or a single item by ID
- Validate input using a Pydantic model or equivalent validation approach
- Handle at least one basic error or invalid request case cleanly

```python
# Example response shape
{
  "id": 1,
  "title": "Write API tests",
  "done": false
}
```

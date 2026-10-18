# Student Management API

A RESTful Student Management API built with Python, FastAPI, and a database layer. The API supports creating, listing, retrieving, updating, and deleting student records.

## Features

- Add a student
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete a student
- Interactive API documentation with Swagger UI

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLite (if configured in `database.py`)

## Project Structure

```text
Student-Management-API/
├── main.py
├── database.py
├── requirements.txt
└── README.md
```

## Setup

Use Python 3.10 or later.

1. Open a terminal in the project folder.
2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the API:

   ```bash
   python -m uvicorn main:app --reload
   ```

4. Open the interactive documentation:

   http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/students` | Retrieve all students |
| POST | `/students` | Add a student |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Example Student Request

This is an example request body. Match field names and data types to the `Student` model in your `main.py`.

```json
{
  "name": "Nithish Reddy",
  "date_of_birth": "2004-05-15",
  "email": "nithish@example.com",
  "phone": "9876543210",
  "course": "CSE AIML",
  "address": "Hyderabad"
}
```

## Testing

Run the API locally and use the Swagger UI at `/docs` to test each endpoint.

## Possible Future Improvements

- Add authentication and authorization
- Add pagination and search
- Improve validation and error handling
- Deploy the API to a hosting platform

## Author

Nithish Reddy

## License

For educational and learning purposes.

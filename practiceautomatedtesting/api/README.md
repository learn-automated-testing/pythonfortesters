# Python API Tests

This is a Python-based API test suite for the Practice Automated Testing application. The tests are written using pytest and the requests library.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
API_BASE_URL=https://api.practiceautomatedtesting.com
```

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with HTML report:
```bash
pytest --html=report.html
```

To run specific test files:
```bash
pytest tests/test_book_api.py
pytest tests/test_auth_api.py
```

To run tests with verbose output:
```bash
pytest -v
```

## Test Structure

- `tests/conftest.py`: Contains shared fixtures and configuration
- `tests/test_book_api.py`: Tests for the book API endpoints
- `tests/test_auth_api.py`: Tests for the authentication API endpoints

## Features

- CRUD operations for books
- Authentication testing
- Search and filtering
- Pagination
- Sorting
- Price range filtering
- Category filtering

## Requirements

- Python 3.9+
- pytest
- requests
- pytest-html
- python-dotenv 
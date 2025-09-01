# Flask Book API

A simple Flask-based API for interacting with Google Books and providing book summaries.

## Folder Structure

```
flask-book-api/
│
├── .venv/              # Python virtual environment (ignored by git)
├── services/           # Service modules (business logic, API integrations)
├── utils/              # Utility/helper functions
├── templates/          # HTML templates for Flask (if using Flask views)
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Setup

1. **Clone the repository:**
   ```
   git clone <repo-url>
   cd flask-book-api
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv .venv
   # On Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # On Windows CMD:
   .venv\Scripts\activate.bat
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and update values as needed.

5. **Run the Flask app:**
   ```
   flask run
   ```

## Features

- Search books using Google Books API
- Optional ML-based summarization
- Configurable via `.env` file

## Notes

- Sensitive files like `.env` and `.venv` are ignored by git.
- For higher Google Books quota, set your API key in `.env`.
- For troubleshooting PowerShell script activation, set execution policy:
  ```
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## License

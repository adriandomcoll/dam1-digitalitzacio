# Prototip4 Project

## Overview
Prototip4 is a Flask-based web application designed for user authentication and management. It provides a secure login system and interacts with a MySQL database to store user information.

## Project Structure
```
prototip4
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── config.py             # Configuration settings for the application
│   ├── dao
│   │   └── user_dao.py       # Data Access Object for user interactions
│   ├── models
│   │   └── user.py           # User model definition
│   ├── services
│   │   └── auth_service.py    # Authentication logic
│   ├── routes
│   │   └── auth.py           # Authentication routes
│   ├── utils
│   │   └── db.py             # Database utility functions
│   └── schemas
│       └── user_schema.py     # User data validation schema
├── tests
│   └── test_auth.py          # Unit tests for authentication functionality
├── BBDD
│   └── tapat_mysql.sql       # SQL schema and initial data for the database
├── requirements.txt           # Project dependencies
├── .env.example               # Example environment variables
├── Dockerfile                 # Instructions for building a Docker image
└── README.md                  # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd prototip4
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Import the SQL schema from `BBDD/tapat_mysql.sql` into your MySQL database.

5. **Configure environment variables**:
   - Copy `.env.example` to `.env` and fill in the required values.

6. **Run the application**:
   ```
   python src/app.py
   ```

## Usage
- The application exposes a `/login` endpoint for user authentication. You can send a POST request with the username and password in JSON format to authenticate users.

## Testing
- Unit tests for the authentication functionality can be run using:
   ```
   python -m unittest tests/test_auth.py
   ```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
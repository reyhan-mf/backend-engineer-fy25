# Backend Engineer Test Project

A RESTful API service built with Flask that provides user authentication and item management functionality. The application implements JWT-based authentication and includes features for creating, reading, updating, and deleting items.

## Features

- User authentication (registration and login)
- JWT-based authorization
- CRUD operations for items
- Pagination support for item listing
- Input validation
- Secure password hashing with bcrypt

## Tech Stack

- Python 3.x
- Flask 3.0.2
- Flask-JWT-Extended 4.6.0
- bcrypt 4.1.2
- email-validator 2.1.1
- SQLite (for data storage)

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
  - Required fields: `email`, `password`
  - Returns: Success message

- `POST /auth/login` - Login user
  - Required fields: `email`, `password`
  - Returns: JWT access token

### Items

- `GET /items` - List all items (with pagination)
  - Query parameters: 
    - `page` (default: 1)
    - `limit` (default: 10, max: 100)
  - Returns: Paginated list of items

- `POST /items` - Create a new item (requires authentication)
  - Required fields: `name`
  - Optional fields: `description`, `status`
  - Returns: Item ID and success message

- `GET /items/<item_id>` - Get a specific item
  - Returns: Item details

- `PUT /items/<item_id>` - Update an item (requires authentication)
  - Optional fields: `name`, `description`, `status`
  - Returns: Success message

- `DELETE /items/<item_id>` - Delete an item (requires authentication)
  - Returns: Success message

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend_engineer_test_fy25
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

The server will start on `http://localhost:5000` by default in debug mode.

## Using the API with Postman

### Setting Up Postman

1. Download and install [Postman](https://www.postman.com/downloads/)
2. Create a new Collection called "Backend Engineer Test"
3. Set up a collection variable for the base URL:
   - Click on the collection → Variables
   - Add a variable named `base_url` with initial value `http://localhost:5000`

### Authentication Flow

1. **Register a User**
   - Method: `POST`
   - URL: `{{base_url}}/auth/register`
   - Headers: 
     ```
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "email": "user@example.com",
         "password": "securepassword"
     }
     ```

2. **Login**
   - Method: `POST`
   - URL: `{{base_url}}/auth/login`
   - Headers:
     ```
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "email": "user@example.com",
         "password": "securepassword"
     }
     ```
   - After successful login, copy the JWT token from the response

3. **Set Up JWT Authentication**
   - In the collection's Variables, add a new variable `jwt_token`
   - Paste the token from the login response
   - In the collection's Authorization tab:
     - Type: `Bearer Token`
     - Token: `{{jwt_token}}`

### Making API Requests

#### Create an Item
- Method: `POST`
- URL: `{{base_url}}/items`
- Authorization: Inherited from collection
- Body (raw JSON):
  ```json
  {
      "name": "Test Item",
      "description": "Test Description",
      "status": "pending"
  }
  ```

#### Get All Items
- Method: `GET`
- URL: `{{base_url}}/items`
- Query Params (optional):
  - `page`: 1
  - `limit`: 10

#### Get Single Item
- Method: `GET`
- URL: `{{base_url}}/items/1`

#### Update Item
- Method: `PUT`
- URL: `{{base_url}}/items/1`
- Authorization: Inherited from collection
- Body (raw JSON):
  ```json
  {
      "name": "Updated Item",
      "description": "Updated Description",
      "status": "completed"
  }
  ```

#### Delete Item
- Method: `DELETE`
- URL: `{{base_url}}/items/1`
- Authorization: Inherited from collection

### Testing Tips

1. Use Postman's environment variables to manage different configurations (development, testing, production)
2. Save example responses for each request
3. Use the "Tests" tab to write automated tests for your API calls
4. Use collection runner to test the entire API flow

### Common Issues

1. **401 Unauthorized**: Check if your JWT token is:
   - Present in the request
   - Not expired
   - Properly formatted in the Authorization header

2. **400 Bad Request**: Verify that:
   - All required fields are present
   - Field values match the expected format
   - Content-Type header is set to application/json

3. **403 Forbidden**: Ensure you're:
   - Using a valid JWT token
   - Trying to modify only your own items

## Security Features

- Password hashing using bcrypt
- JWT-based authentication
- Input validation for email and password
- Authorization checks for item operations
- Protection against unauthorized item modifications 


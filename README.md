# N-Queens Puzzle API

This project creates an API using FastAPI to calculate solutions for the N-Queens problem and store them in a PostgreSQL database. You can generate solutions for different values of `n` (size of the chessboard and number of queens) and retrieve the stored solutions via API endpoints.

## Features
- Calculate solutions to the N-Queens problem for any board size `n` between 1 and 11.
- Store the solutions in a PostgreSQL database.
- Retrieve all stored solutions or a specific solution by its order.

## Requirements
- Docker
- Docker Compose

## How to Run the Project

1. Clone the repository:
    ```
    git clone https://github.com/gmorales96/eight_queens_puzzle.git
    ```

2. Create a .env file with the following variables:
    ```
    DB_USER=admin
    DB_PASSWORD=mypassword
    DB_NAME=eight_queens
    ```

3. Build and run the project using Docker Compose:
    ```
    docker-compose up --build -d
    ```

4. To stop the project:
    ```
    docker-compose down
    ```

## API Endpoints

### Generate N-Queens Solutions
To generate solutions for an `n x n` chessboard, make the following `POST` request:

```
curl --location 'http://127.0.0.1:3003/api/solutions/generate' \
--header 'Content-Type: application/json' \
--data '{
  "n": 8
}'
```

The `n` parameter specifies the size of the chessboard and the number of queens.
Example: Setting `"n": 8` generates solutions for the 8-Queens problem.

### Retrieve All Stored Solutions
To fetch all solutions stored in the database, use this `GET` request:

```
curl --location 'http://127.0.0.1:3003/api/solutions'
```

### Retrieve a Specific Solution
To retrieve a specific solution by its order in the database, use this `GET` request:

```
curl --location 'http://127.0.0.1:3003/api/solutions/2'
```

Replace `2` with the order of the solution you want to retrieve. For example, use `/solutions/1` to get the first stored solution.

### Testing
Unit tests are provided for the N-Queens solution logic using pytest. To run the tests:

1. Create a virtual environment:
    ```
    python -m venv .
    ```

2. Activate the virtual environment:
    - On Linux
        ```
        source bin/activate
        ```
    - On Windows
        ```
        .\Scripts\activate
        ```

2. Install the necessary dependencies, including pytest:
    ```
    python -m pip install -r requirements.txt
    ```

3. Run the tests:
    ```
    pytest .\tests\test_queens_problem.py
    ```
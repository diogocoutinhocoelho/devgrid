# Weather API - Diogo Coutinho Coelho

This project provides a weather data collection service using the Open Weather API. The service collects and stores weather data for specified cities and provides endpoints to access the stored data.

## Features

- **POST /weather**: Initiates the collection of weather data for specified cities.
- **GET /weather/<user_defined_id>**: Retrieves the collected weather data for a given user-defined ID.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Docker

### Installation

1. **Clone the repository:**

    ```bash
    git clone <https://github.com/diogocoutinhocoelho/devgrid.git>
    cd devgrid
    ```

2. **Set up a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the environment variable:**

    Create a `.env` file in the root of the project and add your OpenWeather API key:
    ```env
    OPENWEATHER_API_KEY=your_openweather_api_key_here
    ```

### Running the Application

1. **Run the application:**

    ```bash
    python run.py
    ```

2. **The application will be available at:**

    ```
    http://127.0.0.1:5000/
    ```

### Running with Docker

1. **Build the Docker image:**

    ```bash
    docker build -t weather_api .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 weather_api
    ```

### API Endpoints

#### POST /weather

Initiates the collection of weather data for the specified cities.

**Request Body:**
```json
{
  "user_defined_id": "unique_id",
  "city_ids": [3439525, 3439781]
}
```

**Response:**
- **202 Accepted**

#### GET /weather/<user_defined_id>

Retrieves the collected weather data for the provided `user_defined_id`.

**Response:**
- **200 OK** with JSON data if the user-defined ID is found.
- **404 Not Found** if the user-defined ID is not found.

### Testing

To run the tests:

```bash
pytest --cov=app tests/
```

### Project Structure

```
devgrid/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── utils.py
│   ├── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_views.py
│
├── Dockerfile
├── requirements.txt
├── README.md
├── run.py
└── .env
```

### Technical Decisions

- **Flask**: Chosen for its simplicity and ease of use for building web APIs.
- **SQLite**: Used for simplicity in this example; it's lightweight and easy to set up.
- **aiohttp and asyncio**: Used for handling asynchronous HTTP requests to the Open Weather API.
- **Docker**: To containerize the application for easy deployment.

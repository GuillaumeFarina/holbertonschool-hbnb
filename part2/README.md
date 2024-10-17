# HBnB Clone Application

## Project Overview

The **HBnB Clone** application is a modular Python application that follows best development practices for the Presentation, Business Logic, and Persistence layers. It is developed with **Flask** for the web side and uses an in-memory repository for temporary data storage, which will be replaced by a database later in the project.

This project also implements the **Facade** design pattern to simplify interactions between these layers.

## Project Structure

The project organization is modular to allow better maintainability and scalability. Here is the directory structure:
```
hbnb/
├── app/
│   ├── __init__.py                # Initializes the Flask application
│   ├── api/
│   │   ├── __init__.py            # Initializes the API endpoints
│   │   ├── v1/
│   │       ├── __init__.py        # Version 1 of the API
│   │       ├── users.py           # Endpoints for users
│   │       ├── places.py          # Endpoints for places
│   │       ├── reviews.py         # Endpoints for reviews
│   │       ├── amenities.py       # Endpoints for amenities
│   ├── models/
│   │   ├── __init__.py            # Initializes the data models
│   │   ├── user.py                # Data model for users
│   │   ├── place.py               # Data model for places
│   │   ├── review.py              # Data model for reviews
│   │   ├── amenity.py             # Data model for amenities
│   ├── services/
│   │   ├── __init__.py            # Initializes the services
│   │   ├── facade.py              # Implements the Facade design pattern
│   ├── persistence/
│       ├── __init__.py            # Initializes the persistence layer
│       ├── repository.py          # In-memory repository for object storage
├── run.py                         # Entry point to run the Flask application
├── config.py                      # Application configuration
├── requirements.txt               # List of project dependencies
├── README.md                      # Description of project
```

Instructions to Run the Application

### Prerequisites

- **Python 3.x** must be installed on your machine.
- The packages listed in `requirements.txt` must be installed.

### Installation Steps

1. **Clone the project from GitHub** :

   ```bash
   git clone https://github.com/holbertonschool-hbnb.git
   cd holbertonschool-hbnb/part2
   ```

2. **Install dependencies** : Run the following command to install the necessary packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application** : Once everything is installed, start the application with:

   ```bash
   python3 run.py
   ```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Description of Important Files

- **`run.py`** : The main file to start the Flask application.
- **`config.py`** : Configuration file to define global settings and security keys.
- **`app/`** : Contains all the application modules, organized into different layers (API, models, services, persistence).
- **`app/api/`** : Manages the API endpoints for the current version.
- **`app/models/`** : Contains business logic classes like `User`, `Place`, `Review`, etc.
- **`app/services/`** : Contains the Facade design pattern to coordinate interactions between different layers.
- **`app/persistence/`** : Contains an in-memory repository for object storage. This repository will be replaced by a database in a later part of the project.

## Dependencies

The `requirements.txt` file contains the following packages:

- **flask**
- **flask-restx**

Install them by running the command :

```bash
pip install -r requirements.txt
```

## Coming Soon

In future parts of the project, the current in-memory persistence layer will be replaced by a database solution using SQLAlchemy. The API will also be enriched with additional features.

## AUTHORS

@GuillaumeFarina \
@Pizzapanda92
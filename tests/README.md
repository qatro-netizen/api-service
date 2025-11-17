"""
api-service
------------

A RESTful API service for data management.

### Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### Running the Service

To start the service, run the following command:

```bash
python app.py
```

### API Endpoints

The service exposes the following API endpoints:

- `GET /users`: Returns a list of all users.
- `POST /users`: Creates a new user.
- `GET /users/{id}`: Returns a user by ID.
- `PUT /users/{id}`: Updates a user by ID.
- `DELETE /users/{id}`: Deletes a user by ID.

### API Documentation

The API documentation can be found at `http://localhost:5000/docs`.

### Database Configuration

Database configuration is stored in `config.py`. Ensure to update the database credentials accordingly.

"""

import os
import sys
from functools import wraps

def configure_logger(level='INFO'):
    import logging.config

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': sys.stdout,
                'formatter': 'default'
            }
        },
        'root': {
            'level': level,
            'handlers': ['wsgi']
        }
    })

if __name__ == '__main__':
    configure_logger(level='DEBUG')
    from app import app

    app.run(debug=True, host='localhost', port=5000)
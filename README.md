# gogolook

Package version

- Python 3.9.6
- Flask 2.2.2
- pytest 7.2.1

### Build image/database

    docker-compose up -d

You will get a container named `gogolook` and you can send the request to `localhost:8000` port.

### Run in local env

Install requirements in your local virtual env.

    pip install -r requirements.txt

Run app.py

    python -u app.py

### Unit Test

Run pytest

    pytest -s tests/test_task.py

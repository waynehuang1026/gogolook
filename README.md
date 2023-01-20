# gogolook

Package version

- Python 3.9.6
- Flask 2.2.2
- pytest 7.2.1

### Build image/database

    $ docker-compose up -d

You will get a container named `gogolook:latest`, and then you can run the container


## Run in local

Install requirements in your virtual env.

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

Run app.py

    $ python -u app.py

## Unit Test

Run pytest

    $ pytest -s tests/test_task.py

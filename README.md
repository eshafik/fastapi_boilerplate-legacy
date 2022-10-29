## Python version: 3.9 or above

# Run:
1. ``pip install -r requirements.txt``
2. `uvicorn main:app --reload`

# sqlalchemy migrations hints:
Change `alembic.ini` file:

`sqlalchemy.url = postgresql://user:pass@host/dbname`

Ensure this exists in `alembic/env.py` for auto schema generation:

`target_metadata = Base.metadata`

1. create migrations file: `alembic revision --autogenerate -m "updated email column on user table"`
2. migrate: `alembic upgrade head`
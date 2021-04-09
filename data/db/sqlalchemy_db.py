import os
import sqlalchemy as db


def generate_db_uri(
        driver: str = "postgres",
        user: str = None,
        password: str = None,
        host: str = None,
        port: int = 5432,
        db: str = None
):
    """
    Generate a database URI string with optional overrides for any env variable
    @param driver: default "postgres"
    @param user
    @param password
    @param host
    @param port: default 5432
    @param db
    @return:
    """
    driver = os.getenv("DB_DRIVER") or driver
    user = os.getenv("DB_USER") or user
    password = os.getenv("DB_PASSWORD") or password
    host = os.getenv("DB_HOST") or host
    port = os.getenv("DB_PORT") or port
    db = os.getenv("DB_NAME") or db

    for uri_key, uri_val in [("user", user), ("password", password), ("host", host), ("db", db)]:
        if uri_val == None:
            raise RuntimeError(f"Incomplete DB URI component given: '{uri_key}'")

    return f"{driver}://{user}:{password}@{host}:{port}/{db}"

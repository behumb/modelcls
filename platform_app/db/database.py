import contextlib
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

SQLALCHEMY_DATABASE_URL = str(os.getenv('DATABASE_URL', "sqlite:///./db/sql_app.db"))

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()


@contextlib.contextmanager
def get_session(cleanup=False):
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()

    if cleanup:
        Base.metadata.drop_all(engine)


@contextlib.contextmanager
def get_conn(cleanup=False):
    conn = engine.connect()
    Base.metadata.create_all(engine)

    yield conn
    conn.close()

    if cleanup:
        Base.metadata.drop_all(engine)

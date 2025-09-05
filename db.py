
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLite_DB_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLite_DB_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your ORM models (e.g., class User(Base): ...)
Base = declarative_base()

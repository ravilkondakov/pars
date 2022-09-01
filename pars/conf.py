import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

def get_engine():
    engine = create_engine(
        f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:5432/{os.getenv("DB_NAME")}',
        echo=True, future=True)
    return engine

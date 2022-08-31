from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@db:5432/url_shorter', echo=True, future=True)

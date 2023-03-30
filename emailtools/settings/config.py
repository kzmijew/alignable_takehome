import os 
from sqlalchemy import create_engine

class PGConnector():
    def __init__(self):
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_DATABASE = os.getenv('DB_DATABASE')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')

    def get_connection(self):
        conn_str = f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}'
        engine = create_engine(conn_str)
        conn = engine.connect()
        return(conn)



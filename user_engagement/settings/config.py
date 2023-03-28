import os 
from dotenv import load_dotenv

load_dotenv()

class PGConnector():
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_PASSWORD = os.getenv('DB_PASSWORD')


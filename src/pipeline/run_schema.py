import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

MIGRATIONS_DIR = Path(__file__).resolve().parents[2] / "migrations"

print(MIGRATIONS_DIR)
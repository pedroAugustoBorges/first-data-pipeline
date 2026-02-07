import psycopg2
import os
from dotenv import load_dotenv
import logging

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

def psql_connection_test():
    conn = None
    
    logging.info('Connecting to the PostgreSQL')
    try:
        conn = psycopg2.connect(
         host = POSTGRES_HOST,
            database = POSTGRES_DB,
            user = POSTGRES_USER,
            password = POSTGRES_PASSWORD,
            port = POSTGRES_PORT
        )
        

        cur = conn.cursor()
        
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        
        logging.info(db_version)
        
        cur.close()
    
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f'Connection was wrong {error}')
        
    finally:
        if conn is not None:
            conn.close()
            
            logging.info('Database connection closed')
            
            
def psql_connection():
    logging.info('Creating connection...')
    
    try:
        conn = psycopg2.connect(
            host = POSTGRES_HOST,
            database = POSTGRES_DB,
            user = POSTGRES_USER,
            password = POSTGRES_PASSWORD,
            port = POSTGRES_PORT
        )
    
        return conn

    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f'Error while connection {error}')
        




    
    
            
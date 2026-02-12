import psycopg2
from psycopg2 import sql
import logging


# idempotent_function
def create_table(psql_conn):
    logging.info('Creating table')
    query = """
    CREATE TABLE IF NOT EXISTS MEMBERS(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        discord_id VARCHAR(255) UNIQUE,
        motivation_member VARCHAR(255) NOT NULL
    )
    """
    
    try:
        
        with psql_conn.cursor() as curr:
            
            psql_conn.autocommit=True
            curr = psql_conn.cursor()
            
            curr.execute(query)
            
    
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f'Error while creating table {error}')
        return
    
    logging.info('Table created')
    
def alter_table(psql_conn, column):
    logging.info('Updating table')

    query = sql.SQL("""
    ALTER TABLE MEMBERS ADD COLUMN IF NOT EXISTS {} TIMESTAMP
    """).format(sql.Identifier(column))
    try:
        curr = psql_conn.cursor()
        
        psql_conn.autocommit = True
        
        curr.execute(query, column)
        
        
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f" Error while alter table with query: {query} - {error}")
        return
    
    logging.info('Table changed')


def drop_table(psql_conn):
    query = """
    DROP TABLE MEMBERS
    """
    try:
        curr = psql_conn.cursor()
        
        curr.execute(query)
        
        psql_conn.cursor()
        
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error while drop table with {query} - {error}")
        return
    
    logging.info("Table dropped")
    
    
    
    
    
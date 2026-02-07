import psycopg2
import logging


# idempotent_function
def create_table(psql_conn):
    query = """
    CREATE TABLE IF NOT EXISTS MEMBERS(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        discord_id VARCHAR(255) UNIQUE,
        motivation_member VARCHAR(255) NOT NULL
    )
    """
    
    try:
        psql_conn.autocommit=True
        curr = psql_conn.cursor()
        
        curr.execute(query)
        
        curr.close()
    
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f'Error while creating table {error}')
        


    
    
    
    
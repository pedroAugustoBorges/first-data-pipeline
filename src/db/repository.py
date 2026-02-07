import psycopg2
import logging

def insert_member(psql_conn, member):
    query = """
    INSERT INTO MEMBERS(name, discord_id, motivation_member)
    VALUES(%s, %s, %s)
    ON CONFLICT(discord_id)
    DO UPDATE SET   
    name = EXCLUDED.name,
    motivation_member = EXCLUDED.motivation_member
    """
    
    try:
        curr = psql_conn.cursor()
        
        psql_conn.autocommit = True
        
        curr.execute(query, (member['name'], member['discord_name'], member['reason_to_code']))
        
        curr.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error while inserting member {member} - {error}")
        
    
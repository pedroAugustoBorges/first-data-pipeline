from core.logging_config import init_logger
from db.connection import psql_connection_test, psql_connection
from db.schema import create_table, alter_table, drop_table
from ingestion.get_data import get_selfdev_members

def main():
    init_logger()
    psql_connection_test()
    conn = psql_connection()
    create_table(conn)
    alter_table(conn, 'datetime_created')
    drop_table(conn)
    


if __name__ == '__main__':
    main()
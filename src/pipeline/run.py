from core.logging_config import init_logger
from db.connection import psql_connection_test, psql_connection
from db.schema import create_table
from ingestion.get_data import get_selfdev_members

def main():
    init_logger()
    psql_connection_test()
    conn = psql_connection()
    create_table(conn)
    get_selfdev_members(conn)
    


if __name__ == '__main__':
    main()
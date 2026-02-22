import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from core.logging_config import init_logger

load_dotenv()

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

MIGRATIONS_DIR = Path(__file__).resolve().parents[2] / "migrations"


def ensure_migrations_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS schema_migrations (
                        version VARCHAR(50) PRIMARY KEY,
                        checksum TEXT NOT NULL,
                        applied_at TIMESTAMP DEFAULT NOW()
                    );
                    """)
        
    conn.commit()
    

def get_applied_version(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT version FROM schema_migrations;")
        rows = cur.fetchall()

        return {row[0] for row in rows}
    
    


def calculate_checksum(content):
    import hashlib
    return hashlib.sha256(content.encode()).hexdigest()



def apply_migration(conn, file_path):
    version = file_path.name.split("_")[0]
    
    with open(file_path, "r", encoding="utf-8") as f:
        sql_script= f.read()
        
    checksum = calculate_checksum(sql_script)


    logging.info(f"Applying migration {file_path.name}")
    
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql_script)
                cur.execute("""
                            INSERT INTO schema_migrations (version, checksum)
                            VALUES (%s, %s)
                            """, (version, checksum))
        logging.info(f"Migration {version} applied successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Migration {version} failed {error}")
        raise


def validate_existing_migrations(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT version, checksum FROM schema_migrations")
        applied = dict(cur.fetchall())
        print(applied)
        
        for file_path in MIGRATIONS_DIR.glob("*.sql"):
            version = file_path.name.split("_")[0]
            
            if version in applied:
                with open(file_path, "r", encoding = "utf-8") as f:
                    content = f.read()
                
                current_checksum = calculate_checksum(content)
                
                if current_checksum != applied[version]:
                    raise RuntimeError(
                        f"Migration {version} was modified after being applied"
                    )
                    
def run_migrations(conn):
    """
    Decet if exists modification in a some migration
    """
    
    file_name = __file__.split('\\')[-1]
    logging.info(f"Running {file_name}")
    
    ensure_migrations_table(conn)
    validate_existing_migrations(conn)

    applied_version =  get_applied_version(conn)
    migrations_files = list(MIGRATIONS_DIR.glob("*.sql"))
    
    
    for file_path in migrations_files:
        version = file_path.name.split("_")[0]
        
        if version not in applied_version:
            apply_migration( conn, file_path)
            

    logging.info(f"""Migration process completed
                 Versions loaded: {[applied for applied in applied_version]} from {[str(migration).split("\\")[-1] for migration in migrations_files]}""")
    
    



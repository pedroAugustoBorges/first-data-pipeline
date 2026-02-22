import pandas as pd
from transform.enrich import create_datetime
from db import repository


def load_loaded_at(conn):
    ids = repository.select_ids(conn)
    
    random_date = create_datetime(len(ids))
    
    data = list(zip(random_date, ids))
    
    repository.insert_loaded_at(conn, data)
    

    
    
    


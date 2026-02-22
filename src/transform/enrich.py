import pandas as pd
from extract.extract_json import extract_data
from ingestion.create_mock_date import random_date


def create_datetime(limit):
    return random_date(limit)

         
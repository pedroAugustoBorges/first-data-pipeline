import random
import pandas as pd
from datetime import datetime, timedelta

min_year = 2023
max_year = datetime.now().year


start= datetime(min_year, 1, 1, 00, 00, 00)
print(f'starts: {start}')

years = max_year - min_year + 1
print(f'years: {years}')

end = start + timedelta(days= 365 * years)
print(f"end: {end}")

def randon_date(limit):
    dates = []
    for i in range(0, limit):
        print(f"start + (end-start): {start + (end-start)}")
        print(f' random {random.random()}')
        random_date = start + (end-start) * random.random()
        print(random_date)
        dates.append(random_date)

print(randon_date(5))
        
        
import json
import logging


def get_selfdev_members():
    with open('data/raw/data.json') as json_file:
        data = json.load(json_file)
        return data['selfdev_members']
        
            
import json
from pathlib import Path
import logging


def get_selfdev_members(file_path):
    
    with open(file_path, encoding= 'UTF-8') as json_file:
        data = json.load(json_file)
        return data['selfdev_members']
        
            

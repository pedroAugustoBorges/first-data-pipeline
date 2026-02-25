from src.ingestion import get_data

def test_extract_json_corret():
    keys = ['name', 'discord_name', 'reason_to_code']
    
    result = get_data.get_selfdev_members()[0]
    
    assert set(result.keys()) == set(keys)
    



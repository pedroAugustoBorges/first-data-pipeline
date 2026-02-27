from ingestion import get_data
from config.settings import DATA_RAW_DIR

def test_all_members_have_required_keys():
    
    members = get_data.get_selfdev_members( DATA_RAW_DIR / "data.json")
    
    print(members)
    
    REQUIRED_KEYS = {'name', 'discord_name', 'reason_to_code'}

    for member in members:
        assert REQUIRED_KEYS.issubset(member.keys())
    
def test_exists_members():
    members = get_data.get_selfdev_members(DATA_RAW_DIR / "data.json")
    
    assert True if len(members) != 0 else False
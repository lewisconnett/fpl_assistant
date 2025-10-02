from data.loader import initialise_app
from core.player_search import find_player_by_id
import pprint

def test():
    print('test without initialisation...')
    
    result = find_player_by_id(123)
    print(f'Result: {result}')
    
    # Initialize data
    initialise_app()

    # Test with valid ID (replace 123 with a known player ID)
    result = find_player_by_id(123)
    pprint.pprint(result)
    
if __name__ == "__main__":
    test()
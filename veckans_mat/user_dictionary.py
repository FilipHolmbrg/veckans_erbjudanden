def get_dictionary(user: int) -> dict:
    if user == 1:
        user_dict = {
                    'carbonara': ['pasta', 'bacon', 'ägg', 'grädde', 'parmesan'],
                    'högrev med potatis': ['högrev', 'potatis'],
                    'korvstroganoff': ['falukorv', 'ris', 'gröna ärtor', 'tomatpuré', 'passerade tomater', 'grädde'],
                    }
        
    else:
        user_dict = None
        
    return user_dict
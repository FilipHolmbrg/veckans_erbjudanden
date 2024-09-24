#imports
import re

def match_recipe(data: dict, user_dict: dict) -> dict:
    veckans_recept_förslag = {recipe: [] for recipe in user_dict.keys()}

    for key, values in user_dict.items():
        # print(key, values)
        current_recipe_list = [] 
        for value in values:
            for item in data['name']:
                if value.upper() in item:
                    pattern = fr'\b{item}\b' #avoid that 'ägg' is mixed up with 'fläsklägg', 'påskägg', 'pålägg'
                    # print(key, value, item)
                    # print(item, pattern)
                    match = re.search(pattern, value)
                    # veckans_recept_förslag.update({key: item})
                    if not value in current_recipe_list:
                        current_recipe_list.append(value)
        
        veckans_recept_förslag.update({key: current_recipe_list})
    
    return veckans_recept_förslag
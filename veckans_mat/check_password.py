import requests

def check_connection(password: str) -> bool:
    #random url that worked at the current time
    url = "https://ereklamblad.se/api/squid/v2/dealerfront?r_lat=57.694554&r_lng=12.206504&r_radius=2500&limit=12&order_by=name&types=paged%2Cincito"
    headers = {
                'Content-Type': 'application/json',  # Non required argument
                'X-Api-Key': password  # Using X-Api-Key header as required
                }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        my_response = True
    else:
        my_response = False
    response.close()
    
    return my_response
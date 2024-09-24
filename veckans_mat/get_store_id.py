import requests

def fetch_id(store_name: str, password: str, store_no: int) -> str:
    
        headers = {
                    'Content-Type': 'application/json',  # Non required argument
                    'X-Api-Key': password  # Using X-Api-Key header as required
                    }
        if store_no == 1:
            url = "https://ereklamblad.se/api/squid/v2/dealerfront?r_lat=57.694554&r_lng=12.206504&r_radius=2500&limit=12&order_by=name&types=paged%2Cincito"

        """Fetch id for store which updates every week"""
        # Make a request to the API
        response = requests.get(url, headers=headers)
        # Ensure the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Loop through the data and extract the desired fields
            for item in data:
                catalogs = item.get("catalogs", [])
                for catalog in catalogs:
                    # print(catalog)
                    if catalog['label'] == store_name:
                        catalog_id = catalog.get("id")
                        return catalog_id
                    
        else:
            raise Exception("Store id not found due to unsuccessful response")
            
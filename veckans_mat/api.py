#Imports
import requests
from time import sleep

def fetch_offers(password: str, store_id: str, store_no: int) -> tuple:
    """Function to get weely offers based of object attributes"""
    # General url
    if store_no == 1:
        url = "https://ereklamblad.se/api/squid/v4/rpc/get_offers"  
    # Create dict used for population of data and creation of datafram
    offer_dict = {
            'validity': [],
            'name': [],
            'price': [],
            'unit': [],
            'save': [],
            'brand': [],
            }
    # Description of items to parse later
    description_list = []
    page_size = 24
    # Prepare request body
    data = {
            "where": {
                "publication_ids": [store_id]  # The publication ID you want to filter by
                    },
            "page": {
                "page_size": page_size  # Max number of items per page
                    }
            }
    
    headers = {
                        'Content-Type': 'application/json',  # Non required argument
                        'X-Api-Key': password  # Using X-Api-Key header as required
                        }
    
    for i in range(3): # Each iteration gives different results, so we need to pickup data many times to be sure to get all.
        sleep(.1)
        after_cursor = None  # Start without any cursor (first page)
        has_next_page = True
        
        while has_next_page:
            sleep(.1) # Pause between pages.
            # Add after_cursor if it's available (for next pages)
            
            if after_cursor:
                data["page"]["after_cursor"] = after_cursor
            else:
                data["page"].pop("after_cursor", None)  # Remove after_cursor if starting from the first page

            response = requests.post(url, json=data, headers=headers)
            
            # Check the response status code
            if response.status_code == 200:
                response_data = response.json()
                
                # Extract and print offers
                offers = response_data.get("offers", [])

                for offer in offers:
                    offer_dict['validity'].append(offer['validity']['to'])
                    offer_dict['name'].append(offer['name']) 
                    offer_dict['price'].append(offer['price'])
                    description_list.append(offer['description'])

                # Handle pagination
                page_info = response_data.get("page_info", {})
                after_cursor = page_info.get("last_cursor", None)  # Get the cursor for the next page
                has_next_page = page_info.get("has_next_page", False)  # Check if there is another page
                
            else:
                break
            
    return (description_list, offer_dict)
import requests

import requests

def get_item_details(item_id, region="na", lang="en"):
    api_url = f"https://api.arsha.io/v2/{region}/item"
    # Request parameters
    params = {
        "id": item_id,
        "lang": lang
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200: # Check if the request was successful (status code 200)
            
            result = response.json() # Parse the response JSON
           
            return result[0]["name"], result[0]["lastSoldPrice"]  # Return the item name and lastSoldPrice
        else:
            # print(f"Error: {response.status_code} - {response.text}")
            return None, None
    except Exception as e:
         # print(f"Error: {e}")
        return None, None

def get_market_prices(region, main_category, sub_category):

    api_url = f"https://api.arsha.io/v2/{region}/GetWorldMarketList"

    # Request parameters
    params = {
        "mainCategory": main_category,
        "subCategory": sub_category
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()
            # Process and display the prices with item names and last sold price
            process_prices(result)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def process_prices(result):
    # Process each item in the result
    for item in result:
        # Extract relevant information
        item_id = item["id"]
        current_stock = item["currentStock"]
        total_trades = item["totalTrades"]
        base_price = item["basePrice"]

        # Get item name and last sold price using the additional API call
        item_name, last_sold_price = get_item_details(item_id)

        # Display information with item name and last sold price
        if(item_name != None): #Ignore items that dont have an ID
            print(f"Item Name: {item_name}, ID: {item_id}, Stock: {current_stock}, Trades: {total_trades}, Base Price: {base_price}, Last Sold Price: {last_sold_price}")

# Execute the program
reg="na"
reg = input("Enter your region (NA): ").lower()
mc = input("Enter the main category: ")
sc = ""
sc = input("Enter the sub category: (hit enter for n/a): ")

get_market_prices(reg, mc, sc)

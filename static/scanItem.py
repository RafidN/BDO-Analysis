import requests

def get_item_prices(item_id, region="na"):
    api_url = f"https://api.arsha.io/v2/{region}/item"

    # Request parameters
    params = {
        "id": item_id
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()

            # Process and display the prices for all enhancement levels
            process_prices(result)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")


def process_prices(result):
    # Process each enhancement level for the item
    for item_data in result:
        # Extract relevant information
        enhance_level = item_data["minEnhance"]
        current_stock = item_data["currentStock"]
        total_trades = item_data["totalTrades"]
        base_price = item_data["basePrice"]
        last_sold_price = item_data["lastSoldPrice"]

        # Display information for each enhancement level
        print(
            f"Enhancement Level: {enhance_level}, Stock: {current_stock}, Trades: {total_trades}, Base Price: {base_price}, Last Sold Price: {last_sold_price}")


# Specify the item ID for which you want to get prices
item_id_to_check = 11629  # You can change this ID as needed

# Execute the program
get_item_prices(item_id_to_check)
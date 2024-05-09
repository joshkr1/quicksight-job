import datetime
import requests
import json

# Function to fetch data from TradeView
def fetch_tradeview_data():
    try:
        # Example URL for fetching trade data from TradeView
        url = 'https://api.tradeview.com/get_trades'
        
        # Example request headers (replace with actual headers)
        headers = {'Authorization': 'Bearer YOUR_API_KEY'}
        
        # Make a GET request to fetch trade data
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            trade_data = json.loads(response.text)
            return trade_data
        else:
            # Print error message if request fails
            print("Error fetching trade data. Status code:", response.status_code)
            return None
    except Exception as e:
        # Print error message if an exception occurs
        print("An error occurred while fetching trade data:", e)
        return None

# Function to process and transform trade data (example implementation)
def process_trade_data(trade_data):
    if trade_data:
        processed_data = []
        for trade in trade_data:
            try:
                # Example processing: extract timestamp and cost
                timestamp = datetime.datetime.fromtimestamp(trade['timestamp'])
                cost = trade['cost']
                processed_data.append((timestamp, cost))
            except KeyError as e:
                # Print error message if required data is missing
                print("KeyError: Missing key in trade data:", e)
        return processed_data
    else:
        return []

# Function to calculate average trade cost between 7am and 8am
def calculate_average_trade_cost(trade_data):
    # Filter trades between 7am and 8am
    trades_7_to_8 = [(time, cost) for time, cost in trade_data if 7 <= time.hour < 8]
    
    # Calculate average trade cost
    if trades_7_to_8:
        average_trade_cost = sum(cost for _, cost in trades_7_to_8) / len(trades_7_to_8)
        return average_trade_cost
    else:
        return None

# Main function
def main():
    # Fetch trade data from TradeView
    tradeview_data = fetch_tradeview_data()
    if tradeview_data is not None:
        # Process trade data
        processed_data = process_trade_data(tradeview_data)
        
        # Calculate average trade cost between 7am and 8am
        average_cost_7_to_8 = calculate_average_trade_cost(processed_data)
        if average_cost_7_to_8 is not None:
            print("Average trade cost between 7am and 8am:", average_cost_7_to_8)
        else:
            print("No trades between 7am and 8am")
    else:
        print("Error fetching trade data. Exiting...")

if __name__ == "__main__":
    main()


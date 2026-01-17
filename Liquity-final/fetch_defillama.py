
import requests
import json

def fetch_liquity_data():
    try:
        # 1. Fetch Protocol Data (TVL breakdown by token)
        # Liquity V2 might be listed separately or under Liquity using 'liquity-v2' or similar
        # We will check 'liquity' and look for v2 chains/tokens or search for 'bold'
        
        print("Fetching Protocol TVL data...")
        response = requests.get("https://api.llama.fi/protocol/liquity-v2") 
        
        if response.status_code == 404:
             # Fallback: Try fetching 'liquity' and checking for multiple versions or breakdown
             print("Liquity V2 endpoint not found, checking main Liquity endpoint...")
             response = requests.get("https://api.llama.fi/protocol/liquity")

        if response.status_code == 200:
            data = response.json()
            
            # Helper to print token breakdown if available
            if 'tokens' in data:
                 print("\n--- Current Token Breakdown ---")
                 # Iterate to find latest data
                 # Note: Structure is usually data['tokens'][chain][token_symbol] = amount
                 # Or data['tvl'][date]... dependent on endpoint structure. 
                 # The /protocol/ endpoint returns granular chainTvl and tokensInUsd
                 
                 # Let's verify 'currentChainTvls' first
                 if 'currentChainTvls' in data:
                     print(f"Chain Breakdown: {json.dumps(data.get('currentChainTvls',{}), indent=2)}")
                 
                 if 'tokensInUsd' in data:
                      # We want the latest breakdown
                      print(f"Token Breakdown (USD): {json.dumps(data.get('tokensInUsd', []), indent=2)}")
            
            # Check for wstETH, WETH, rETH specifically in the latest data point
            # This is a heuristic search in the output
            print("\nRaw Data Snippet (First 500 chars):")
            print(str(data)[:500])
            
        else:
            print(f"Failed to fetch protocol data. Status: {response.status_code}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_liquity_data()

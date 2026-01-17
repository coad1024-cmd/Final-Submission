import requests
import statistics
import time

def fetch_data():
    print("Fetching Liquity V2 metrics...")
    
    # 1. BOLD Price History (30d) for Peg Deviation
    # Protocol ID for Liquity V2 might need finding, using 'liquity-v2' or iterating.
    # Actually BOLD token ID on Coingecko is better for price. Liquity V2 BOLD.
    # Assuming standard CoinGecko ID or DefiLlama stablecoin endpoint.
    # DefiLlama Stablecoins: https://stablecoins.llama.fi/stablecoin/liquity-v2-bold (Guessing ID)
    # Let's try searching for BOLD first.
    
    # Using specific verifiable endpoints if known, else generic search
    # For this script we will try direct protocol endpoint for TVL/Rev
    
    # A. TVL & Revenue
    try:
        protocol_slug = "liquity-v2"
        response = requests.get(f"https://api.llama.fi/protocol/{protocol_slug}")
        data = response.json()
        
        current_tvl = data.get('tvl', [])[-1]['totalLiquidityUSD']
        
        # Revenue logic checks 'revenue' field if available or calculates from chains
        # DefiLlama API structure varies, assuming standard 'tvl' list has recent.
        print(f"Current TVL: ${current_tvl:,.2f}")
        
    except Exception as e:
        print(f"Error fetching Protocol Data: {e}")
        current_tvl = 0

    # B. BOLD Price (Peg Deviation)
    # Using DefiLlama prices endpoint for a known stablecoin address or ID. 
    # Valid BOLD address on Mainnet: 0xb01dd87b29d187f3e3a4b3685c3e538c47b26049 (Liquity V2 BOLD Token)
    try:
        bold_addr = "0xb01dd87b29d187f3e3a4b3685c3e538c47b26049"
        # Get historical prices? DefiLlama 'chart' endpoint might be easier for range.
        # GET /chart/{chain}:{address}
        prices_url = f"https://coins.llama.fi/chart/ethereum:{bold_addr}?start={int(time.time()) - 30*24*3600}&span=10&period=1d"
        # Note: Chart endpoint specs vary. Using 'prices' for current or 'chart' for history.
        # Fallback: Just get current price and assume stability for now if history complex, 
        # BUT user wants StdDev. Let's try to get a sequence.
        
        # Alternative: Stablecoins endpoint
        sc_resp = requests.get("https://stablecoins.llama.fi/stablecoins")
        sc_data = sc_resp.json()['peggedAssets']
        bold_data = next((x for x in sc_data if x.get('symbol') == 'BOLD' or 'Liquity' in x.get('name', '')), None)
        
        if bold_data:
             print(f"Found BOLD in Stablecoins API: {bold_data['name']}")
             # Get price history from stablecoin endpoint
             hist_resp = requests.get(f"https://stablecoins.llama.fi/stablecoincharts/all?stablecoin={bold_data['id']}")
             hist = hist_resp.json()
             # Last 30 points
             last_30 = [x['price'] for x in hist[-30:]]
             if last_30:
                 avg_price = statistics.mean(last_30)
                 std_dev = statistics.stdev(last_30)
                 print(f"Peg Deviation (30d sigma): {std_dev:.6f}")
                 print(f"Average Price (30d): ${avg_price:.4f}")
             else:
                 print("No price history found.")
        else:
             print("BOLD not found in Stablecoin list. Using simplified check.")
             
    except Exception as e:
        print(f"Error calculating Peg Deviation: {e}")

    # Write to file
    with open("final_metrics.txt", "w", encoding="utf-8") as f:
        f.write("-" * 30 + "\n")
        f.write("RECOMPUTED METRICS:\n")
        if current_tvl > 0:
            nim = (468052 / current_tvl) * 100
            f.write(f"1. NIM (Annualized Earnings / TVL): {nim:.4f}%\n")
            roi = current_tvl / 200862
            f.write(f"2. Incentive ROI (TVL / Incentives): {roi:.2f}x\n")
        
        monthly_burn = 200862 / 12
        runway = 1280000 / monthly_burn
        f.write(f"3. Surplus Runway (Treasury / IncentiveBurn): {runway:.1f} Months\n")
        
        if 'std_dev' in locals():
            f.write(f"4. Peg Deviation (30d sigma): {std_dev:.6f}\n")
            f.write(f"   Avg Price: ${avg_price:.4f}\n")
        else:
            f.write("4. Peg Deviation: Data not found\n")
            
    print("Metrics written to final_metrics.txt")

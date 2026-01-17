import requests
import json
from datetime import datetime

# DefiLlama fees endpoint
url = "https://api.llama.fi/summary/fees/liquity-v2?dataType=dailyFees"

try:
    response = requests.get(url, timeout=30)
    data = response.json()
    
    print("=== Liquity V2 Fee Data from DefiLlama ===\n")
    
    # Get total fees
    if 'totalAllTime' in data:
        print(f"Total All-Time Fees: ${data['totalAllTime']:,.2f}")
    
    if 'total24h' in data:
        print(f"24h Fees: ${data['total24h']:,.2f}")
    
    if 'total7d' in data:
        print(f"7d Fees: ${data['total7d']:,.2f}")
    
    if 'total30d' in data:
        print(f"30d Fees: ${data['total30d']:,.2f}")
    
    # Calculate 2025 totals if daily data available
    if 'totalDataChart' in data:
        chart_data = data['totalDataChart']
        
        # Filter for 2025 data (timestamp >= Jan 1, 2025)
        jan_1_2025 = 1704067200  # Unix timestamp for Jan 1, 2025
        
        q1_fees = 0  # Jan-Mar
        q2_fees = 0  # Apr-Jun
        q3_fees = 0  # Jul-Sep
        q4_fees = 0  # Oct-Dec
        
        for entry in chart_data:
            ts = entry[0]
            fee = entry[1] if len(entry) > 1 else 0
            
            if ts >= jan_1_2025:
                dt = datetime.fromtimestamp(ts)
                month = dt.month
                
                if month <= 3:
                    q1_fees += fee
                elif month <= 6:
                    q2_fees += fee
                elif month <= 9:
                    q3_fees += fee
                else:
                    q4_fees += fee
        
        print(f"\n=== 2025 Quarterly Breakdown ===")
        print(f"Q1 2025: ${q1_fees:,.0f}")
        print(f"Q2 2025: ${q2_fees:,.0f}")
        print(f"Q3 2025: ${q3_fees:,.0f}")
        print(f"Q4 2025: ${q4_fees:,.0f}")
        print(f"2025 Total: ${q1_fees + q2_fees + q3_fees + q4_fees:,.0f}")
    
    # Save full response for inspection
    with open('defillama_raw.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("\nFull response saved to defillama_raw.json")
    
except Exception as e:
    print(f"Error: {e}")
    
    # Try alternate endpoint
    try:
        alt_url = "https://api.llama.fi/protocol/liquity-v2"
        response = requests.get(alt_url, timeout=30)
        data = response.json()
        print(f"\nProtocol data retrieved:")
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"TVL: ${data.get('tvl', 0):,.0f}")
        
        with open('defillama_protocol.json', 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e2:
        print(f"Alternate endpoint error: {e2}")

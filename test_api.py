# test_api.py
import requests
import json

def test_earnings_call_api():
    # API endpoint (local development server)
    url = "http://127.0.0.1:5000/earnings_transcript_summary"
    
    # Sample test data
    test_data = {
        "company_name": "Relience Industries",
        "transcript_text": """
        Good morning everyone. Thank you for joining us for Test Company's Q4 2023 earnings call.
        
        Our financial performance this quarter has been strong, with revenue growth of 15% year-over-year,
        reaching $500 million. Operating margin improved to 25%.
        
        In terms of market dynamics, we're seeing increased demand in the Asian markets,
        particularly in emerging economies. Competition remains intense but we've maintained our market share.
        
        We're excited to announce our expansion plans into European markets, with two new offices
        opening in Berlin and Paris next quarter. We're also investing heavily in R&D.
        
        Regarding environmental initiatives, we've reduced our carbon footprint by 20% this year
        and are on track to meet our 2025 sustainability goals.
        
        On the regulatory front, we're adapting to new data privacy regulations in the EU
        and expect minimal impact on our operations.
        """
    }
    
    # Test health endpoint
    try:
        health_response = requests.get("http://127.0.0.1:5000/health")
        print("\nHealth Check Response:", health_response.json())
    except requests.exceptions.RequestException as e:
        print("\nError checking health endpoint:", str(e))
        return
    
    # Make POST request to the API
    try:
        print("\nSending request to API...")
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=test_data, headers=headers)
        
        # Print response details
        print("\nStatus Code:", response.status_code)
        print("\nResponse Headers:", json.dumps(dict(response.headers), indent=2))
        
        if response.status_code == 200:
            print("\nAPI Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print("\nError Response:")
            try:
                print(json.dumps(response.json(), indent=2))
            except json.JSONDecodeError:
                print(response.text)
            
    except requests.exceptions.RequestException as e:
        print("\nError making request:", str(e))

if __name__ == "__main__":
    test_earnings_call_api()
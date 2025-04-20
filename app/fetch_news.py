
import requests
from datetime import date, timedelta

def fetch_news(ticker, api_key):
    today = date.today()
    last_week = today - timedelta(days=7)

    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from={last_week}&to={today}&token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Filter out items with no 'headline' key
        headlines = [item['headline'] for item in data if 'headline' in item and item['headline']]
        return headlines
    
    return []

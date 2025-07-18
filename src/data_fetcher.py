import requests

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(coin_id="bitcoin", currency="usd"):
    """Fetches live crypto price from CoinGecko."""
    params = {
        "ids": coin_id,
        "vs_currencies": currency
    }
    response = requests.get(COINGECKO_API, params=params)
    if response.status_code == 200:
        return response.json()[coin_id][currency]
    else:
        raise Exception(f"Error fetching price: {response.status_code}")

def get_crypto_news():
    """Fetches crypto-related news using NewsAPI (replace API_KEY)."""
    API_KEY = "YOUR_NEWSAPI_KEY"
    url = f"https://newsapi.org/v2/everything?q=crypto&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()["articles"][:5]
        return [a["title"] for a in articles]
    else:
        return ["No news available."]

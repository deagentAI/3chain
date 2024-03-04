import requests
from constants import CRYPTO_APIKEY

API_KEY = CRYPTO_APIKEY
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

portfolio_cryptos = ['BTC', 'ETH', 'DOT', 'AXS', 'MATIC', 'GALA', 'ALU', 'PBR', 'UFO', 'SHIB', 'ARB', 'DERC', 'FTM', 'LTC', 'PHA']

def get_crypto_data(symbol):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }

    params = {
        'symbol': symbol
    }

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        data = response.json()
        return data['data'][symbol]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data for {symbol}: {e}")
        return None

def get_crypto_prices():
    crypto_data = []
    for crypto_symbol in portfolio_cryptos:
        crypto_info = get_crypto_data(crypto_symbol)
        if crypto_info:
            crypto_data.append(crypto_info)

    response = ""
    for crypto in crypto_data:
        name = crypto['name']
        symbol = crypto['symbol']
        current_price = crypto['quote']['USD']['price']
        percent_change_1h = crypto['quote']['USD']['percent_change_1h']
        percent_change_24h = crypto['quote']['USD']['percent_change_24h']
        percent_change_7d = crypto['quote']['USD']['percent_change_7d']
        market_cap = crypto['quote']['USD']['market_cap']

        response += f"{name} ({symbol}):\n"
        response += f"Current Price: ${current_price:.2f}\n"
        response += f"Percent Change (1 hour): {percent_change_1h:.2f}%\n"
        response += f"Percent Change (24 hours): {percent_change_24h:.2f}%\n"
        response += f"Percent Change (7 days): {percent_change_7d:.2f}%\n"
        response += f"Market Cap: ${market_cap:.2f}\n\n"

    return response

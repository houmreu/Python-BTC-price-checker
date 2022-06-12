import requests
from datetime import datetime

URL = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"

def get_price(coin, currency):
    try:
        response = requests.get(URL.format(coin, currency)).json()
        return response
    except:
        return False

while True:
    date_time = datetime.now()
    date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
    currentBTCPrice = get_price("BTC", "USD")
    if currentBTCPrice:
        print(date_time, "Price:", currentBTCPrice["USD"], "$")
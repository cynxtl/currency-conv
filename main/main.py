import requests

API_KEY = 'fca_live_xY7gobGHVA7xNuqQkg3DCFGISltlPZS4qIFi41qI'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "INR", "EUR", "JPY"]

def convert_currency(base, amount):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return {currency: value * amount for currency, value in data["data"].items()}
    except:
        print("Invalid Currency Input")
        return None

while True:
    base = input("Enter the base currency (q to quit) : ").upper()

    if base == "Q":
        break

    amount = float(input("Enter the Amount to Convert : "))

    data = convert_currency(base, amount)
    if not data:
        continue

    for ticker, value in data.items():
        print(f"{ticker}: {value}")
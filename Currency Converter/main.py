import requests

cur = input().lower()
rates = requests.get(f"http://www.floatrates.com/daily/{cur}.json").json()
rates = {k.upper(): float(v['rate']) for k, v in rates.items()}
cache = {'USD', 'EUR'}
while (exchange_to := input().upper()) != '':
    amount = float(input())
    print("Checking the cache...")
    print("Oh! It is in the cache!" if exchange_to in cache
          else "Sorry, but it is not in the cache!")
    cache.add(exchange_to)
    res = round(amount * rates[exchange_to], 2)
    print(f"You received {res} {exchange_to}.")
import requests

#  KRW- 붙은 코드만 조회하는 경우

url = "https://api.upbit.com/v1/market/all"

resp = requests.get(url)
data = resp.json()

krw_tic = []

for coin in data :
    ticker = coin['market']  # coin is dict

    if ticker.startswith("KRW"):
        krw_tic.append(ticker);

print(krw_tic)
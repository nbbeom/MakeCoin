import pyupbit
import pprint
##비트코인으로 구매 가능한 TICKER 
ticker =  pyupbit.get_tickers(fiat ="BTC")
print(ticker)
print(len(ticker))

##시세 캔들 조회 1분봉
df = pyupbit.get_ohlcv("KRW-BTC","minute1")

print(df)
##시세 캔들 조회 3분봉
df = pyupbit.get_ohlcv("KRW-BTC","minute3")

print(df)
#주봉
df = pyupbit.get_ohlcv("KRW-BTC",interval ="week")

print(df)
## upbit 의 일봉은  아침 9시 부터~ 아침 8시 59분까지 
#일봉
df= pyupbit.get_ohlcv("KRW-BTC",interval = "day", count=1) #1개만 조회
print(df)
#월봉
df= pyupbit.get_ohlcv("KRW-BTC",interval = "month", count=2) #1개만 조회
print(df)

# 현재가격 정보
price = pyupbit.get_current_price("KRW-BTC")
print(price)

#여러 종목 현재가 정보
ticker = ["KRW-BTC","KRW-XRP"]
price = pyupbit.get_current_price(ticker)
print(price)

#모든 종목
ticker = pyupbit.get_tickers(fiat= "KRW")

prices  = pyupbit.get_current_price(ticker)

for k, v in prices.items():
    print(k,v)

#호가 종목
# ask 매도 호가 잔량
# bid 매수 호가 잔량
orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)

#매도호가 총 잔량 매수 호가 총 잔량
orderbooks = pyupbit.get_orderbook("KRW-BTC")

total_ask_size = orderbooks['total_ask_size']
total_bid_size = orderbooks['total_bid_size']

print(total_ask_size)
print(total_bid_size)
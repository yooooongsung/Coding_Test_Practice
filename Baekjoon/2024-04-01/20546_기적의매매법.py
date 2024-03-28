def junhyeon(cash,price):
    stock = 0
    for i in price:
        if i <= cash: #보유한 현금보다 주가가 싸다면
            q = cash // i #살 수 있는 수량
            cash = cash - i * q #보유 현금 업데이트
            stock = stock + q #총 주식 갯수 업데이트

    return stock * price[-1] + cash #자산계산


def seongmin(cash,price):
    stock = 0
    for i in range(10): #인덱스 범위 조정
        if price[i] < price[i+1] and price[i+1] < price[i+2] and price[i+2] < price[i+3]: #3일 연속 상승
            if stock != 0: #가지고 있는 주식이 있다면
                cash = stock * price[i+3] #전량 매도
                stock = 0 #전량 매도

        elif price[i] > price[i+1] and price[i+1] > price[i+2] and price[i+2] > price[i+3]: #3일 연속 하락
            if price[i+3] <= cash: #3일 연속 하락가가 보유 현금보다 싸다면
                q = cash // price[i+3] #살 수 있는 수량
                cash = cash - price[i+3] * q #보유 현금 업데이트
                stock = stock + q #총 주식 갯수 업데이트

    return stock * price[-1] + cash #자산 계산

cash = int(input())
price = list(map(int,input().split()))

if junhyeon(cash,price) > seongmin(cash,price): #준현이의 자산이 크다면
    print('BNP')
elif junhyeon(cash,price) < seongmin(cash,price): #성민의 자산이 크다면
    print('TIMING')
else:
    print('SAMESAME') #같다면

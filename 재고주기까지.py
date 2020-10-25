#재고: 판매를 위해 현재 보유하고 있는 물품들
#안전재고: 갑자기 구매량 변동이 있을 것을 대비하여 미리 확보해 둔 재고
#리드타임: 발주에서 입고까지 걸리는 시간
#안전재고 공식: 일일 최고 판매량 * 최대 리드타임 - 일일 평균 판매량 * 평균 리드타임
#적정재고: 일정한 재고량을 유지해 재고 흐름을 만들고 재고 상황에 유연하게 대처하기 위한 재고 수량
#적정재고 공식: 지연 가능한 리드타임 * 일간 안전 재고량     (단, 구매 주기가 매일 관리가 된다는 전제. 구매 주기가 바뀐다면 적정 재고량은 바뀔 수 있음)
#지연 가능한 최대 리드타임 = 최대 리드타임 - 평균 리드타임
#일간 안전 재고량 = 최대 판매량 - 평균 판매량

#미래 구매량 구하는 방법...
#금주 재고량 = 전주의 재고 + 금주의 구매량 - 금주의 판매량
#재고주기 = 금주 재고량 / 과거 4주 판매 평균
#재고주기 = (전주의 재고 + 금주의 구매량 - 금주의 판매량) / 과거 4주 판매 평균
#최적 구매량 예측 모델은 이 재고주기 식의 항을 정리해서 정리하면 된다
#이때 재고 주기를 안정 재고 주기를 이용하면 안정 재고량 유지, 판매량에 대한 표준편차를 이용하면 안정 재고량을 판단하는 데에 도움

avleadtime = 1
mxleadtime = 2
stock = []
purchase = []
sale = []
purchase_average = []
stock_cycle = []
while True:
    if len(stock) == 0:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b)
        purchase.append(int(a))
        sale.append(int(b))
        stock.append(c)
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" % (purchase, sale, stock))
        print("최대 판매량 : %s" %(max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    elif len(stock) < 3:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    else :
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        #판매량 평균
        d = (sale[-1] + sale[-2] + sale[-3] + sale[-4])/4
        purchase_average.append(d)
        print("판매량 평균 : %s" %purchase_average)

        #재고 주기
        e = stock[-1]/purchase_average[-1]
        stock_cycle.append(round(e,2))
        print("재고주기 : %s" %stock_cycle)
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))
        print("안전 재고 주기: %s" %(((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime))/d))
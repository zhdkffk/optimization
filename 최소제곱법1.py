# 최소 제곱법 구현
#a = {(x-x평균)(y-y평균)}의 합 / {(x-x평균)의 제곱}의 합  (합: 모든 데이터에 대해)
#polyfit = 다항식에 대한 최적화
import csv
import matplotlib.pyplot as plt

sale_data = []
optimal_weight = 0
optimal_xaxis = []
optimal_yaxis = []

with open("sample_data.csv", encoding='utf-8-sig') as data:
    reader = csv.DictReader(data)
    sum_x = 0
    sum_y = 0
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        sale_data.append({'price': price, 'qty': sale_qty})
        sum_x += price
        sum_y += sale_qty
        plt.scatter(price, sale_qty)


import csv

with open("sample_data.csv", encoding='utf-8-sig') as data:
    reader = csv.DictReader(data)
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        print("sale: %d, price: %d" % (sale_qty, price,))

# y=ax+b
# a = 가중치, 최소제곱법 이용
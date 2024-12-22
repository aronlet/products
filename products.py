products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('清輸入價格:')
	products.append([name, price])

print(products)

for p in products:
	print(p[0],'的價格是:', p[1])


# print(products_name, products_price)
# print(products_price)
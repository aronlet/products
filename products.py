products_name = []
products_price = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	products_name.append(name)

	price = input('清輸入價格:')
	if price == 'q':
		break
	products_price.append(price)

print(products_name, products_price)
# print(products_price)
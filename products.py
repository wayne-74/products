import os

products = []#建立空清單
#檢查檔案products有沒有在作業系統，如果有的話讀取檔案
if os.path.isfile('products.csv'):
    print('yeah! 找到檔案了')
    with open('products.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            s = line.strip().split(',')
            name = s[0]
            price = s[1]
            products.append([name, price])
    print(products)
else:
	print('找不到檔案............')

#讓使用者新增購買記錄
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)

#印出所有購買記錄
for p in products:
	print(p[0], '的價格是：' ,p[1])

#寫入檔案
with open('products.csv', 'w', ) as f:
	f.write('商品,價格,\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

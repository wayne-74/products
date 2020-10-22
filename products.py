import os

    
def read_file(filename): #定義讀取檔案為read_file
    products = [] #建立products空清單
    with open(filename, 'r') as f: #開啟檔案並將檔案存成f
        for line in f: #一行一行讀取檔案f
            if '商品,價格' in line:
                continue
            s = line.strip().split(',')
            name = s[0]
            price = s[1]
            products.append([name, price])       
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        products.append([name, price])
    print(products)
    return products

#印出所有購買記錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是：' ,p[1])

#寫入檔案
def wirte_file(filename, products):
    with open(filename, 'w', ) as f:
        f.write('商品,價格,\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('yeah! 找到檔案了')
        products = read_file('products.csv')#執行read_file並存回products
    else:
        print('找不到檔案')

    products = user_input(products)#執行讓使用者新增購買記錄並存回products
    print_products(products)#執行印出products
    wirte_file('products.csv', products)

main()
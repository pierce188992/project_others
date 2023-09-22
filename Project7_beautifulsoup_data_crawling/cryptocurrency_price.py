from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
# 得到一個標籤名稱為"tbody" 的全部元素內容 不包含<tbody>/</tbody>
# 會將子元素節點全部放入list內

prices = {}
for tr in trs[:10]:  # 只要前10個子元素
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

for name, price in prices.items():
    print(f"crytocurrency: {name}")
    print(f"price: {price}")
    print("--------------------")

import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/"
response = requests.get(url)
sp = BeautifulSoup(response.text, "html.parser")

datas = sp.find("div", class_="contents_box02")

title = datas.find("span", "font_black15").text
print(f"Power Color Lottery Draw Date: {title}")

nums = datas.find_all("div", class_="ball_tx ball_green")
# nums = datas.select("div.ball_tx.ball_green")

print(f"Drawn numbers in order:", end=" ")
for index in range(0, 6):
    print(nums[index].text, end=" ")

print(f"\nNumbers in ascending order:", end=" ")
for index in range(6, 12):
    print(nums[index].text, end=" ")

sec_num = datas.find("div", "ball_red").text
print(f"\nSecond area number: {sec_num}")

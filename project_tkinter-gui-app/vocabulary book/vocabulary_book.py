import tkinter as tk
import math
import os


def First():
    global page
    page = 1
    dispData()


def Prev():
    global page
    if page > 1:
        page -= 1
        dispData()


def Next():
    global page
    if page < totalpage:
        page += 1
        dispData()


def Last():
    global page
    page = totalpage
    dispData()


def dispData():
    if datas != None:
        sep1 = tk.Label(frameShow, text="\t", fg="white", width=20, font=("arial", 10))
        sep1.grid(row=0, column=0, sticky="w")
        labe1 = tk.Label(
            frameShow,
            text="vocabulary".ljust(30),
            fg="white",
            bg="black",
            width=30,
            font=("arial", 10),
        )
        labe1.grid(row=1, column=0, sticky="w")
        label2 = tk.Label(
            frameShow,
            text="chinese meaning".ljust(150),
            fg="white",
            bg="black",
            width=80,
            font=("arial", 10),
        )
        label2.grid(row=1, column=1, sticky="w")

        n = 0  # 資料從索引0開始
        row = 2  # 資料從第2列開始
        start = (page - 1) * pagesize

        for eword, cword in datas.items():
            # 顯示目前page的資料
            if n >= start and n < start + pagesize:  # 索引390~399
                label3 = tk.Label(
                    frameShow,
                    text="\t" + "{:30}".format(eword),
                    fg="blue",
                    font=("arial", 10),
                )
                label3.grid(row=row, column=0, sticky="w")
                label4 = tk.Label(
                    frameShow,
                    text="\t" + "{:50}".format(cword),
                    fg="blue",
                    font=("arial", 10),
                )
                label4.grid(row=row, column=1, sticky="w")
                row += 1  # 索引397 原本在第9列 +1 變成在第10列
                if n == 397:
                    label3 = tk.Label(
                        frameShow, text="\t" + " " * 30, font=("arial", 10)
                    )  # 覆蓋原本第10列
                    label3.grid(row=row, column=0, sticky="w")
                    label4 = tk.Label(
                        frameShow, text="\t" + " " * 50, font=("arial", 10)
                    )  # 覆蓋原本第10列
                    label4.grid(row=row, column=1, sticky="w")
                    row += 1  # 變成第11列

            n += 1  # 索引398 跳出for迴圈

        if n == 398:
            label3 = tk.Label(
                frameShow, text="\t" + " " * 30, font=("arial", 10)
            )  # 覆蓋原本第11列
            label3.grid(row=row, column=0, sticky="w")
            label4 = tk.Label(
                frameShow, text="\t" + " " * 50, font=("arial", 10)
            )  # 覆蓋原本第11列
            label4.grid(row=row, column=1, sticky="w")


window = tk.Tk()
window.geometry("500x300")
window.title("Vocabulary book")

page = 1
pagesize = 10

datas = dict()

# 获取当前脚本的绝对目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构建eword.txt的相对路径
file_path = os.path.join(current_dir, "eword.txt")

with open(file_path, "r", encoding="utf-8-sig") as file:
    for line in file:
        eword, cword = line.rstrip("\n").split(",")
        datas[eword] = cword

datasize = len(datas)  # 資料筆數
totalpage = math.ceil(datasize / pagesize)  # 總頁數

# 單字顯示區
frameShow = tk.Frame(window)
frameShow.pack()
labelwords = tk.Label(window, text="")
labelwords.pack()

frameCommand = tk.Frame(window)  # 翻頁按鈕容器
frameCommand.pack()

buttonFirst = tk.Button(frameCommand, text="first page", width=13, command=First)
buttonFirst.grid(row=0, column=0, padx=5, pady=5)
buttonPrev = tk.Button(frameCommand, text="previous page", width=13, command=Prev)
buttonPrev.grid(row=0, column=1, padx=5, pady=5)
buttonNext = tk.Button(frameCommand, text="next page", width=13, command=Next)
buttonNext.grid(row=0, column=2, padx=5, pady=5)
buttonLast = tk.Button(frameCommand, text="last page", width=13, command=Last)
buttonLast.grid(row=0, column=3, padx=5, pady=5)

First()

window.mainloop()

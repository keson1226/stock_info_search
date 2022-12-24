import datetime
import requests

def re_input(talk):
    while True:
        user_input=input(talk)
        try:
            user_input=int(user_input)
        except:
            print('請輸入整數!!\n')
            continue
        else:
            return user_input

def get_info():
    print("歡迎使用台灣股市 日收盤價及月平均收盤價 查找系統!!")
    url="https://www.twse.com.tw/zh/exchangeReport/STOCK_DAY_AVG?response=json&date={}{}"
    date=datetime.date.today()
    year=date.year
    month=date.month
    search_year=None
    search_month=None
    while True:  #跟使用者確認要查找的年份
        user_input=re_input("請輸入要查找的年份: ")
        if user_input<=year and user_input>=1999:
            search_year=user_input
            break
        else:
            print('請輸入有效的年份!!\n')
    
    if search_year==year: #跟使用著確認要查找的月份
        while True:
            user_input=re_input("請輸入要查找的月份: ")
            if user_input<=month and user_input>=1:
                search_month=user_input
                break
            else:
                print('請輸入有效的月份!!\n')
    else:
        while True:
            user_input=re_input("請輸入要查找的月份: ")
            if user_input<=12 and user_input>=1:
                search_month=user_input
                break
            else:
                print('請輸入有效的月份!!\n')
    if search_month<10:
        search_month="0"+str(search_month)
    
    url=url.format(search_year,search_month)+"01&stockNo={}"

    search_stock=None
    while True: # 跟使用者確認要查找的股票編號
        empty_stock="{\"stat\":\"很抱歉，沒有符合條件的資料!\"}"
        user_input = input("請輸入要查找的股票編號: ")
        if requests.get(url.format(user_input)).text==empty_stock:
            print("請輸入有效的股票編號!!")
        else:
            search_stock=user_input
            break
    print("\n正在搜索 {} 年 {} 月 股票編號 {} 的相關資訊....\n".format(search_year,search_month,search_stock))
    return url.format(search_stock)



if __name__=='__main__':
    print(get_info())
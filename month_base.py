import datetime,requests

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
    print("歡迎使用台灣股市 月成交資訊 查找系統!!")
    url="https://www.twse.com.tw/zh/exchangeReport/FMSRFK?response=json&date={}0101&stockNo="
    year=datetime.date.today().year

    search_year=None
    while True:
        user_input=re_input("請輸入要查找的年份: ")
        if user_input <= year and user_input >=1999:
            search_year=user_input
            url=url.format(user_input)
            break
        else:
            print("請輸入有效的年份!!\n")

    search_stock=None    
    while True:
        empty_stock="{\"stat\":\"很抱歉，沒有符合條件的資料!\"}"
        user_input=input("請輸入要查找的股票編號: ")
        if requests.get(url+user_input).text == empty_stock:
            print("請輸入有效的股票編號!!")
        else:
            search_stock=user_input
            url+=user_input
            break
    
    print("\n正在搜索 {} 年 股票編號 {} 的相關資訊....\n".format(search_year,search_stock))
    return url

if __name__=='__main__':
    print(get_info())
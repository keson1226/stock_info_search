import json

import urllib.request as request
import matplotlib.pyplot as plt

import day_base
import month_base

def sort_string(word:str):
    isblank=False
    new_word=""
    word=word.replace("　"," ")
    for i in word:
        if i==" ":
            if not isblank:
                new_word+=" "
            isblank=True
        else:
            isblank=False
            new_word+=i
    return new_word

if __name__=='__main__':
    plt.rcParams['font.sans-serif']=["Taipei Sans TC Beta"]
    print()

    choice=None
    while True:
        n=day_base.re_input("(1)每日股價查找\n(2)每月股價查找\n請選擇要使用的功能: ")
        if n>0 and n<3:
            choice=n
            break
        else:
            print("請輸入有效的數字!!\n")
    print()

    if choice==1:
        url=day_base.get_info()
        req = request.Request(url)

        web_info_json=None
        with request.urlopen(req) as web:
            web=web.read().decode('utf-8')
            web_info_json= json.loads(web)

        data=web_info_json["data"]
        for i in range(len(data)):
            data[i][1]=float(data[i][1])
            temp:str=data[i][0]
            temp=temp.split("/")
            try:
                temp=temp[2]
            except:pass
            else:
                data[i][0]=temp

        month_avg = data.pop(len(data)-1)

        day=[]
        price=[]
        for i in data:
            day.append(i[0])
            price.append(i[1])

        price_high=max(price)
        price_low=min(price)
        price_gap=(price_high-price_low)/9
        price_low-=price_gap/2
        if price_low<0:price_low=0
        ytag=[]
        for i in range(6):
            num=round(price_low+price_gap*i*2,2)
            if num not in ytag:
                ytag.append(num)
        ytag.append(month_avg[1])
        ytag.sort()

        graph_title=sort_string( web_info_json["title"] ) 
        plt.figure(figsize=(8,4.5))
        plt.title(graph_title,fontdict={"fontsize":18,"fontweight":"bold"})
        plt.plot(day,price,"y.-",label="每日收盤價")
        plt.plot([day[0],day[len(day)-1]],[month_avg[1],month_avg[1]],"r--",label=month_avg[0])
        plt.xlabel(web_info_json["fields"][0],fontdict={"fontsize":12})
        plt.ylabel(web_info_json["fields"][1],fontdict={"fontsize":12})
        plt.yticks(ytag)
        plt.legend()
        plt.savefig(graph_title+".png")

        print("搜索完成，已儲存成圖片檔案 --> {}\n\n謝謝您的使用，歡迎下次再來!!".format(graph_title+".png"))

        
        
    

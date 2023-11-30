from itertools import count
from turtle import width
from lib import creatDB ,inputData,PrData,close,addData,UpdateData,serchPh,deleteData,data
ln = '\n'
try:
    account = str(input('請輸入帳號：'))
    password = str(input('請輸入密碼：'))
    if (account == data[0]["帳號"] and password == data[0]["密碼"]) or (account == data[1]["帳號"] and password == data[1]["密碼"]):
        raise
    else :
        raise ValueError

except ValueError as e:
    print('=>帳密錯誤，程式結束')

except:
    while True:
        print('''
---------- 選單 ----------
0 / Enter 離開
1 建立資料庫與資料表
2 匯入資料
3 顯示所有紀錄
4 新增記錄
5 修改記錄
6 查詢指定手機
7 刪除所有記錄
--------------------------''')
        ch1 = input('請輸入您的選擇 [0-7]:')
        if ch1 == '0' or ch1 == '' :
            close()
            break
        elif ch1 == '1':
            creatDB()
            print('=>資料庫已建立')
        elif ch1 == '2':
            inputData()
        elif ch1 == '3':
            PrData()
        elif ch1 == '4':
            addData()
        elif ch1 == '5':
            UpdateData()
        elif ch1 == '6':
            serchPh()
        elif ch1 == '7':
            deleteData()
        else:
            print('=>無效的選擇')

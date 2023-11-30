import json
import sqlite3

with open('pass.json',encoding='utf-8') as a:
    data = json.load(a)
def creatDB()  -> None:
    """
    Creat a database and a member table.
    """
    conn = sqlite3.connect('wanghong.db')
    cursor = conn.cursor()
    cursor.execute('''
    create table if not exists member
    (
        iid  integer primary key autoincrement,
        mname  char(20) not null,
        msex    char(1)  not null,
        mphone  char(15) not null
    );
    ''')
    cursor.close()
    conn.close()
def inputData() -> None:
    '''
    Insert data in to database.
    '''
    conn = sqlite3.connect('wanghong.db')
    cursor = conn.cursor()
    mname = []
    msex = []
    mphone = []
    with open('member.txt',encoding='utf-8') as memlist:
        for line in memlist.readlines():
            memberlist = line.split(',')
            mname.append(memberlist[0])
            msex.append(memberlist[1])
            mPh = str(memberlist[2])
            mphone.append(mPh.strip())
    for i in range (0,6):
        cursor.execute("insert into member(mname, msex, mphone) select ?, ?, ? \
        where not exists(select 1 from member where mname=? and msex=? and mphone=?);" \
        ,(mname[i], msex[i], mphone[i], mname[i], msex[i], mphone[i]))
        conn.commit()
    print(f'=>異動 {conn.total_changes} 筆記錄')
    cursor.close()
    conn.close()
def PrData() -> None:
    '''
    Print database data.
    '''
    conn = sqlite3.connect('wanghong.db')
    cursor = conn.execute(" select * from member ")
    data = cursor.fetchall()
    if len(data) > 0:
        print(f"\n姓名　　　　性別　手機\n-----------------------------")
        for record in data:
            aa=record[1]
            bb=record[2]
            cc=record[3]
            print(f"{aa:\u3000<6}{bb:>2}{cc:\u3000>13}")

    else:
        print('=>查無資料')
    cursor.close()
    conn.close()
def addData() -> None:
    '''
    Insert a new data into table.
    '''
    conn = sqlite3.connect('wanghong.db')
    cursor = conn.cursor()
    addName = input('請輸入姓名:')
    if addName == '':
        print('必須輸入姓名、性別、手機')
    addSex = input('請輸入性別:')
    if addSex == '':
        print('必須輸入姓名、性別、手機')
    addPhone = input('請輸入手機:')
    if addPhone == '':
        print('必須輸入姓名、性別、手機')
    conn.execute("insert into member(mname, msex, mphone) select ?, ?, ? \
        where not exists(select 1 from member where mname=? and msex=? and mphone=?);" \
        ,(addName, addSex, addPhone, addName, addSex, addPhone))
    conn.commit()
    print(f'=>異動 {conn.total_changes} 筆記錄')
    cursor.close()
    conn.close()
def UpdateData() -> None:
    '''
    Update data.
    '''
    conn = sqlite3.connect('wanghong.db')
    cursor = conn.cursor()
    try:
        mname = []
        msex = []
        mphone = []
        with open('member.txt',encoding='utf-8') as memlist:
            for line in memlist.readlines():
                memberlist = line.split(',')
                mname.append(memberlist[0])
                msex.append(memberlist[1])
                mPh = str(memberlist[2])
                mphone.append(mPh.strip())
        ChangName = input('請輸入想修改記錄的姓名:')
        if ChangName in mname:
            raise ValueError
        else:
            raise Exception
    except ValueError as e:
        ChangSex = input('請輸入要改變的性別:')
        ChangPhone = input('請輸入要改變的手機:')
        cursor = conn.execute(" select * from member where mname like ? ",(ChangName,))
        exdata = cursor.fetchall()
        print(f"\n原資料：")
        if len(exdata) > 0:
            for record in exdata:
                print(f"姓名：{record[1]}，性別：{record[2]}，手機：{record[3]}")
        cursor.execute(" update member set msex=?,mphone=? where mname=?; ",(ChangSex,ChangPhone,ChangName))
        conn.commit()
        print(f'=>異動 {conn.total_changes} 筆記錄')
        print(f"修改後資料：")
        print(f"姓名：{ChangName}，性別：{ChangSex}，手機：{ChangPhone}")
        
    except Exception as e:
        print('=>必須指定姓名才可修改記錄')
        
def serchPh() -> None:
    '''
    Input phone number to serch member data.
    '''
    conn = sqlite3.connect('wanghong.db')
    serchPhone = input('請輸入想查詢記錄的手機:')
    cursor = conn.cursor()
    cursor.execute(" select * from member where mphone like ? ",(serchPhone,))
    data = cursor.fetchall()
    if len(data) > 0:
        for record in data:
            print(f"\n姓名　　　　性別　手機\n-----------------------------\n{record[1]:\u3000<6}{record[2]:>2}{record[3]:\u3000>13}")
def deleteData()->None:
    '''
    Delete all in data.
    '''
    conn = sqlite3.connect('wanghong.db')
    conn.execute(" delete from member ")
    conn.commit()
    print(f"=>異動 {conn.total_changes} 筆記錄")
def close() -> None:
    '''
    Close database.
    '''
    conn = sqlite3.connect('wanghong.db')
    conn.close

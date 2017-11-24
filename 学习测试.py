#coding:utf-8
import sqlite3,_thread,time,csv
ZhuanTai=0
ShuJvKu=sqlite3.connect("GuiJi.db")
YouBiao=ShuJvKu.cursor()
wj2=open("cs.txt","w")
csv1=csv.writer(wj2)
try:
    YouBiao.execute("drop table GuiJi")
except:
    pass
YouBiao.execute("CREATE TABLE GuiJi (GuiJi INT)")
def cs1():
    global ZhuanTai
    ShuJvKu=sqlite3.connect("GuiJi.db")
    YouBiao=ShuJvKu.cursor()
    while 1:
        YouBiao.execute("INSERT INTO GuiJi VALUES (1)")
        ZhuanTai=ZhuanTai+1
    ShuJvKu.commit()
    ShuJvKu.close()
def cs2():
    global ZhuanTai
    wj=open("cs.txt","a+")
    while 1:
        wj.write("1\n")
        ZhuanTai=ZhuanTai+1
    wj.flash()
    wj.close()
def cs3():
    global ZhuanTai
    while 1:
        csv1.writerow([1])
        ZhuanTai=ZhuanTai+1
_thread.start_new_thread(cs2, ())
time.sleep(1)
print(ZhuanTai)

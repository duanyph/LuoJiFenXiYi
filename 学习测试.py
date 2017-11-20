#coding:utf-8
import sqlite3
ZhuanTai='20'
ShuJvKu=sqlite3.connect("GuiJi.db")
YouBiao=ShuJvKu.cursor()
try:
    YouBiao.execute("drop table GuiJi")
except:
    pass
YouBiao.execute("CREATE TABLE GuiJi (GuiJi INT)")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
YouBiao.execute("INSERT INTO GuiJi VALUES ("+ZhuanTai+")")
ShuJvKu.commit()
YouBiao.execute("SELECT GuiJi FROM GuiJi")
GuiJi=YouBiao.fetchall()
for JiLu in GuiJi:
    print(JiLu[0])
ShuJvKu.close()
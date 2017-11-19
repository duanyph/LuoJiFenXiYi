#coding:utf-8
'''
Created on 2017年11月15日

@author: duany
'''
from tkinter import *
import threading,time
ZhuanTai=10
BiaoShi=None
GuiJi=[]
X=1
tk1=Tk()
def CaiYang():
    global BiaoShi,ZhuanTai,GuiJi
    while 1:
        GuiJi.append(ZhuanTai)
#         time.sleep(0.01)
        if BiaoShi=="t":
            break
ZiXianCheng=threading.Thread(target=CaiYang, args=())
ZiXianCheng.start()
while 1:
    BiaoShi=input("输入“t”停止采样：")
    if BiaoShi=="t":
        break
Canvas1=Canvas(width=400,height=400)
for Hua in GuiJi:
    Hua=0-Hua+400
    Canvas1.create_rectangle(X,Hua,X,Hua)
    X=X+1
Canvas1.pack()
tk1.mainloop()
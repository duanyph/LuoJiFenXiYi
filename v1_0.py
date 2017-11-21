#coding:utf-8
'''
Created on 2017年11月15日

@author: duany
'''
from tkinter import *
import _thread,time
ZhuangTai=0
GuiJi=[0]*500
# cly=0
tk1=Tk()
tk1.resizable(0,0)
X=1
Canvas1=Canvas(width=500,height=200)
Canvas1.pack()
# tk.geometry("800x800")
def HuiZhi():
#     time.sleep(1)
#     print(cly)
    global ZhuangTai
    while 1:
        ZhuangTai=int(input(">"))
_thread.start_new_thread(HuiZhi, ())
while 1:
    GuiJi.pop()
    GuiJi.insert(0,ZhuangTai)
    Canvas1.delete(ALL)
    for Hua in GuiJi:
        Hua=0-Hua+200
        Canvas1.create_rectangle(X,Hua,X,Hua)
        X=X+1
    tk1.update()
    X=1
#     cly=1+cly
#coding:utf-8
'''
Created on 2017.11.15

@author: duany
'''
from tkinter import *
import _thread,time
from RPi import GPIO 
ZhuangTai=0
GuiJi=[0]*300
#~ cyl=0
X=1
tk1=Tk()
tk1.resizable(0, 0)
Canvas1=Canvas(width=300,height=200)
Canvas1.pack()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# tk1.geometry("800x800")
def CaiYang():
    #~ global cyl
    global GuiJi
    while 1:
        GuiJi.pop()
        GuiJi.insert(0,GPIO.input(7))
        time.sleep(0.000001)
        #~ cyl=1+cyl
_thread.start_new_thread(CaiYang, ())
#~ time.sleep(1)
#~ print(cyl)
while 1:
    Canvas1.delete(ALL)
    for Hua in GuiJi:
        Hua=(0-Hua)*100+150
        Canvas1.create_rectangle(X,Hua,X,Hua)
        X=X+1
    tk1.update()
    X=1
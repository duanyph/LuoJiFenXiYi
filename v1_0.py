#coding:utf-8
'''
@author: duany
'''
from tkinter import *
import _thread,time
from RPi import GPIO 
ZhuangTai=0
<<<<<<< HEAD
GuiJi=[0]*300
cyl=0
tk1=Tk()
tk1.resizable(0, 0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
X=1
Canvas1=Canvas(width=300,height=200)
=======
GuiJi=[0]*500
# cly=0
tk1=Tk()
tk1.resizable(0,0)
X=1
Canvas1=Canvas(width=500,height=200)
>>>>>>> db1921573c198cf3b55b41f93af3ab77c7f3f271
Canvas1.pack()
# tk.geometry("800x800")
"""def HuiZhi():
    global cyl
    time.sleep(2)
    print(cyl)"""
#~ _thread.start_new_thread(HuiZhi, ())
while 1:
    GuiJi.pop()
    GuiJi.insert(0,GPIO.input(7))
    Canvas1.delete(ALL)
    for Hua in GuiJi:
<<<<<<< HEAD
        Hua=(0-Hua)*100+150
=======
        Hua=0-Hua+200
>>>>>>> db1921573c198cf3b55b41f93af3ab77c7f3f271
        Canvas1.create_rectangle(X,Hua,X,Hua)
        X=X+1
    tk1.update()
    X=1
    #~ cyl=1+cyl

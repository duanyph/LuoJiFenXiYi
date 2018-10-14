#coding:utf-8
'''
Created on 2017.11.15

@author: duany
'''
from tkinter import *
import threading,time,csv
from RPi import GPIO 
YingJiao=18
cyl=0
ZhuanTai=""
X=1
tk1 = Tk()
tk1.geometry("500x200")
tk1.resizable(1, 0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(YingJiao,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
LiShi=open("LiShi.csv","w")
csv1=csv.writer(LiShi)
def CaiYang():
    global ZhuanTai,LiShi
    global cyl
    while ZhuanTai!="t":
        csv1.writerow([GPIO.input(YingJiao),time.time()])
        cyl=cyl+1
    LiShi.flush()
    LiShi.close()
class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
# create scrolled canvas
vscrollbar = AutoScrollbar(tk1)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(tk1, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)
canvas1 = Canvas(tk1,yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set,height=200)
canvas1.grid(row=0, column=0, sticky=N+S+E+W)
vscrollbar.config(command=canvas1.yview)
hscrollbar.config(command=canvas1.xview)
# make the canvas expandable
tk1.grid_rowconfigure(0, weight=1)
tk1.grid_columnconfigure(0, weight=1)
# create canvas contents
frame1 = Frame(canvas1)
# frame1.rowconfigure(1, weight=1)
# frame1.columnconfigure(1, weight=1)
canvas1.create_window(0, 0, anchor=NW)
ZiXianCheng=threading.Thread(target=CaiYang, args=())
ZiXianCheng.start()
time.sleep(1)
print(cyl)
while ZhuanTai!="t":
    ZhuanTai=input("输入“t”停止采样：")
for JiLu in csv.reader(open("LiShi.csv","r")):
    JiLu=(0-int(JiLu[0]))*100+150
    canvas1.create_rectangle(X,JiLu,X,JiLu)
    X=X+1
frame1.update_idletasks()
canvas1.config(scrollregion=canvas1.bbox("all"))
tk1.mainloop()

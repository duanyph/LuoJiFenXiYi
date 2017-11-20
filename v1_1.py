#coding:utf-8
'''
@author: duany
'''
from tkinter import *
import threading,time,sqlite3
from RPi import GPIO 
cyl=0
ZhuanTai=""
X=1
tk1 = Tk()
tk1.geometry("400x200")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
ShuJvKu2=sqlite3.connect("GuiJi.db")
YouBiao2=ShuJvKu2.cursor()
def CaiYang():
    global ZhuanTai,cyl
    ShuJvKu=sqlite3.connect("GuiJi.db")
    YouBiao=ShuJvKu.cursor()
    try:
        YouBiao.execute("drop table GuiJi")
    except:
        pass
    YouBiao.execute("CREATE TABLE GuiJi (GuiJi INT)")
    ShuJvKu.commit()
    while ZhuanTai!="t":
        YouBiao.execute("INSERT INTO GuiJi VALUES ("+str(GPIO.input(7))+")")
        cyl=cyl+1
    ShuJvKu.commit()
    ShuJvKu.close()
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
time.sleep(3)
print(cyl)
while ZhuanTai!="t":
    ZhuanTai=input("输入“t”停止采样：")
YouBiao2.execute("SELECT GuiJi FROM GuiJi")
GuiJi=YouBiao2.fetchall()
for JiLu in GuiJi:
    JiLu=(0-JiLu[0])*100+150
    canvas1.create_rectangle(X,JiLu,X,JiLu)
    X=X+1
frame1.update_idletasks()
canvas1.config(scrollregion=canvas1.bbox("all"))
ShuJvKu2.close()
tk1.mainloop()
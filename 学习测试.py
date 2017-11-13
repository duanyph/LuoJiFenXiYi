from tkinter import *
import threading,time
ZhuangTai=0
GuiJi=[0]*400
cly=0
Suo=threading.RLock()
# tk.geometry("800x800")
def CaiYang():
    global ZhuangTai
    global GuiJi
    global cly
    while 1:
        GuiJi.pop()
        GuiJi.insert(0,ZhuangTai)
        cly=1+cly
def HuiZhi():
    global GuiJi
    tk1=Tk()
    X=400
    Canvas1=Canvas(width=400,height=400)
    Canvas1.pack()
    while 1:
        Suo.acquire()
        Canvas1.delete(ALL)
        for Hua in GuiJi:
            Canvas1.create_oval(X,Hua,X,Hua)
            X=X-1
        tk1.update()
        X=400
        Suo.release()
threading.Thread(target=CaiYang,args=()).start()
threading.Thread(target=HuiZhi,args=()).start()
time.sleep(1)
print(cly)
while 1:
    ZhuangTai=input("X:")
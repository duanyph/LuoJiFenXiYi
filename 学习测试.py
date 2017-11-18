from tkinter import *
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
tk1 = Tk()
tk1.geometry("400x400")
vscrollbar = AutoScrollbar(tk1)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(tk1, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)
canvas1 = Canvas(tk1,yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set,width=800,height=400,bg="red")
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
canvas1.create_oval(500,100,500,100)
frame1.update_idletasks()
canvas1.config(scrollregion=canvas1.bbox("all"))
tk1.mainloop()
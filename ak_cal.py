from tkinter import *
import re
import math
root=Tk()
root.title("Ankit Group")

root.minsize(height=200,width=145)

t1=Entry(root,font=("",15,""),bd=4)
t1.grid(row=1,column=1,sticky="w",columnspan=4)

def settxt(x):
    t1.insert("end",x)

def setoperation(x):
    t1.insert("end",x)

def equals():
    exp=t1.get()
    ans=eval(exp)
    t1.delete(0, END)
    t1.insert("end",ans)

def clear():
    a=len(t1.get())
    t1.delete(a-1, END)

but1=Button(root,text=1,height=3,width=6,command=lambda x=1:settxt(x))
but1.grid(row=11,column=1)
but2=Button(root,text=2,height=3,width=6,command=lambda x=2:settxt(x))
but2.grid(row=11,column=2)
but3=Button(root,text=3,height=3,width=6,command=lambda x=3:settxt(x))
but3.grid(row=11,column=3)
but4=Button(root,text=4,height=3,width=6,command=lambda x=4:settxt(x))
but4.grid(row=12,column=1)
but5=Button(root,text=5,height=3,width=6,command=lambda x=5:settxt(x))
but5.grid(row=12,column=2)
but6=Button(root,text=6,height=3,width=6,command=lambda x=6:settxt(x))
but6.grid(row=12,column=3)
but7=Button(root,text=7,height=3,width=6,command=lambda x=7:settxt(x))
but7.grid(row=13,column=1)
but8=Button(root,text=8,height=3,width=6,command=lambda x=8:settxt(x))
but8.grid(row=13,column=2)
but9=Button(root,text=9,height=3,width=6,command=lambda x=9:settxt(x))
but9.grid(row=13,column=3)
but0=Button(root,text=0,height=3,width=6,command=lambda x=0:settxt(x))
but0.grid(row=14,column=2)

but12=Button(root,height=3,width=6,text="+",command=lambda x="+":setoperation(x))
but12.grid(row=11,column=4)
but13=Button(root,text="-",height=3,width=6,command=lambda x="-":setoperation(x))
but13.grid(row=12,column=4)
but14=Button(root,text="/",height=3,width=6,command=lambda x="/":setoperation(x))
but14.grid(row=13,column=4)
but15=Button(root,text="*",height=3,width=6,command=lambda x="*":setoperation(x))
but15.grid(row=14,column=4)

but16=Button(root,text="=",height=3,width=6,command=lambda x="=":equals())
but16.grid(row=14,column=3)

but17=Button(root,text="CLR",height=3,width=6,command=lambda :clear())
but17.grid(row=14,column=1)


root.mainloop()

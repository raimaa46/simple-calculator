from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
        pass
    elif text=="C":
        scvalue.set("")
        screen.update()

        pass
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()
root = Tk()
root.geometry("500x526")
root.title("calculator by Raimaa")
scvalue=StringVar()
scvalue.set("")
screen =Entry(root, textvar=scvalue , font = "lucida 40 bold")
screen.pack(fill=X , ipadx=8 , ipady=10 , padx=10)
f1=Frame(root,bg='grey')
b=Button(f1, text="9" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=18 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="8" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT ,padx=18 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="7" , padx=28 , pady=16 ,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="/" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT ,padx=18 , pady=12)
b.bind("<Button-1>", click)
f1.pack()
f1=Frame(root,bg='grey')
b=Button(f1, text="6" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=20 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="5" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT ,padx=18 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="4" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="*" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
f1.pack()
f1=Frame(root,bg='grey')
b=Button(f1, text="3" , padx=30 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=20 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="2" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT ,padx=18 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="1" , padx=28 , pady=16 ,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="-" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
f1.pack()
f1=Frame(root,bg='grey')
b=Button(f1, text="0" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=20 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="C" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="=" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
b=Button(f1, text="+" , padx=28 , pady=16,font="lucida 20 bold")
b.pack(side=LEFT , padx=12 , pady=12)
b.bind("<Button-1>", click)
f1.pack()
root.mainloop()


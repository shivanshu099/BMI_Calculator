from tkinter import font
from ttkbootstrap import*
import ttkbootstrap as tb

def bmi(wei,hei):
    #weight in kg and height in m
    b=wei/(hei)**2
    if(b<18):
        ma="underweight"
    elif(b<18.5):
       ma="thin for height"
    elif(b>=18.6  and b<=24.9):
        ma="healthy weight"
    elif(25>=18.6 and b<=29.9):
        ma="over weight"
    elif(b>30):
        ma="obesity"
    return ma


def resp():
    x=wei_var.get()
    y=hei_var.get()
    ans=bmi(x,y)
    lbl.config(text="your bmi is "+ans)
    print("your bmi is",bmi(90,2))

'''******************'''

root=tb.Window(themename="cyborg")
name_var=tk.IntVar()
root.title('bmi_calcu')
root.geometry('400x400')
root.minsize(400,400)
root.maxsize(400,400)
my_label=tb.Label(text="bmi_calcu",font=("Comic Sans MS",20))
my_label.pack(pady=20)
wei_var=tb.IntVar()
hei_var=tb.IntVar()
#########
wei_label=tb.Label(root, text = 'weight(kg)', font=('calibre',10, 'bold'))
wei_entery=tb.Entry(root,textvariable = wei_var, font=('calibre',10,'normal'))
hei_label=tb.Label(root, text = 'height(m)', font=('calibre',10, 'bold'))
hei_entery=tb.Entry(root,textvariable = hei_var, font=('calibre',10,'normal'))
show=tb.Button(text="show",bootstyle="danger,outline",command=resp)
#########

wei_label.pack(pady=10)
wei_entery.pack(padx=10)
hei_label.pack(pady=10)
hei_entery.pack(padx=10)
show.pack(pady=25)
#########
lbl = tk.Label(text = "",font=("Comic Sans MS",20)) 
lbl.pack(pady=10)
#print(font.families())
#print(font.families())
root.mainloop()






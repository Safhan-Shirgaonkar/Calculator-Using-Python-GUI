from tkinter import*
root=Tk()
root.title("CALCULATOR")
a=Entry(root,width=50,borderwidth=6)
a.grid(row=0,column=0, columnspan=3, padx=10,pady=10)

def button_click(number):
    current=a.get()
    a.delete(0,END)
    a.insert(0,current+str(number))

def button_clear():
    a.delete(0,END)

def button_add():
    firstnumber=a.get()
    global fnum
    global math
    math="Addition"
    fnum=int(firstnumber)
    a.delete(0,END)

def button_substract():
    firstnumber=a.get()
    global fnum
    global math
    math="Substraction"
    fnum=int(firstnumber)
    a.delete(0,END)
    
def button_multiply():
    firstnumber=a.get()
    global fnum
    global math
    math="Multiplication"
    fnum=int(firstnumber)
    a.delete(0,END)

def button_divide():
    firstnumber=a.get()
    global fnum
    global math
    math="Division"
    fnum=int(firstnumber)
    a.delete(0,END)



def button_equal():
    second_number=a.get()
    a.delete(0,END)
    if math=="Addition":
        a.insert(0, fnum + int(second_number))
    if math=="Substraction":
        a.insert(0, fnum - int(second_number))
    if math=="Multiplication":
        a.insert(0, fnum * int(second_number))
    if math=="Division":
        a.insert(0, fnum / int(second_number))
    
    


#Defining Buttons
b0=Button(root,text="0",padx=50,pady=25,command=lambda:button_click(0))
b1=Button(root,text="1",padx=50,pady=25,command=lambda:button_click(1))
b2=Button(root,text="2",padx=50,pady=25,command=lambda:button_click(2))
b3=Button(root,text="3",padx=50,pady=25,command=lambda:button_click(3))
b4=Button(root,text="4",padx=50,pady=25,command=lambda:button_click(4))
b5=Button(root,text="5",padx=50,pady=25,command=lambda:button_click(5))
b6=Button(root,text="6",padx=50,pady=25,command=lambda:button_click(6))
b7=Button(root,text="7",padx=50,pady=25,command=lambda:button_click(7))
b8=Button(root,text="8",padx=50,pady=25,command=lambda:button_click(8))
b9=Button(root,text="9",padx=50,pady=25,command=lambda:button_click(9))
badd=Button(root,text="+",padx=50,pady=25,command=button_add)
bsubstract=Button(root,text="-",padx=50,pady=25,command=button_substract)
bmultiply=Button(root,text="x",padx=50,pady=25,command=button_multiply)
bdivide=Button(root,text="/",padx=50,pady=25,command=button_divide)
bequal=Button(root,text="=",padx=50,pady=25,command=button_equal)
bclear=Button(root,text="Clear",padx=40,pady=25,command=button_clear)



#button on screen
b0.grid(row=4,column=0)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

badd.grid(row=1,column=3)
bsubstract.grid(row=2,column=3)
bmultiply.grid(row=3,column=3)

bdivide.grid(row=4,column=3)
bequal.grid(row=4,column=2)
bclear.grid(row=4,column=1)

root.mainloop()
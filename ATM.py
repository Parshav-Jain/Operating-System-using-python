from tkinter import *
root = Tk()
root.title('ATM')
root.geometry('200x250')
balance = 10000
#FUNCTIONS
def start(event):
    if pin.get() == '1234' :
        
        main_page()
    else:
        error.config(text = 'Try Again !')

def check_bal():
    Top = Toplevel()
    a = Label(Top , text ='Your balnce is ' , font = ('Arial',17))
    balance_val = Label(Top,text = balance , font = ('Arial',15))
    a.pack()
    balance_val.pack()

def withdraw():
    Top2 = Toplevel()
    def start_withdraw():
        if inte.get() > balance:
            error.config(text = 'Not Enough Money ')
        else:
            error.config(text = 'Left Value is : ')
            left_val.config( text = balance - inte.get())
            left_val.pack()
    inte = IntVar()            
    with_input = Entry(Top2 , width = 20 , borderwidth = 6 , textvariable = inte)
    btn = Button(Top2,text = 'Start',command = start_withdraw)
    error = Label(Top2 , text = '',font = ('Arial',17))
    left_val = Label(Top2 , text = '' , font = ('Arial',15)) 
    with_input.pack()
    btn.pack()
    error.pack()
    left_val.pack()


def main_page():
    heading.destroy()
    pin.destroy()
    start.destroy()
    error.destroy()
    root.geometry('400x300')

    top = Frame(root)
    bottom = Frame(root)    
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

    step_1 = Label(root,text = 'Press 1 for Balance',font = ('Arial',19))
    step_2 = Label(root,text = 'Press 2 for Withdraw',font = ('Arial',19))
    
    btn1 = Button(root,text = '1',command = check_bal,font = ('Arial',17))
    btn2 = Button(root,text = '2',command = withdraw , font= ('Arial',17))
    step_1.pack()
    step_2.pack()
    btn1.pack(in_= bottom, side=BOTTOM)
    space = Label(root,text = '      ')
    space.pack(in_ = bottom , side = BOTTOM)
    btn2.pack(in_ = bottom, side= BOTTOM)

heading = Label(root,text  = 'ATM',font = ('Arial',18))
heading.pack(pady= 10 , fill = X)

pin = Entry(root,width = 20 , show = '' , textvariable = StringVar())
pin.pack()

start = Button(root,text ='OK' , command = start)
start.pack()
error = Label(root,text = '',font = ('Arial',16))
error.pack(pady = 5)

root.bind('<Return>' , start )




root.mainloop()

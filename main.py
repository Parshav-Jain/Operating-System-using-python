from tkinter import*
import os
import random
import time
root = Tk()
root.resizable(0,0)
root.geometry('853x450')
root.title('PJs O.S')
 
def clock():
    
    hour = time.strftime('%H')
    min_ = time.strftime('%M')
    sec  = time.strftime('%S')
    status_bar.config(text = 'Time : '+hour + ':' + min_ + ':' + sec)
    status_bar.after(1000 , clock)

def password_func(event):
    if password.get() == '1234' :
        homepage()
    else:
        password.config(show = '')
def open_password():
    
    def generate():
        value = random.choice(passwords_lst)
        pass_here.config(text = value)

    Top1= Toplevel()
    passwords_lst = ['123456','password','qwerty' , '$hekh h@nniZ' , 'p@rrh@v j@!n' , '@nur@gmail.c0m' , '!@#$%^&*<>']
    heading_password = Label(Top1 , text = 'P@ssw0rd Gener@t0r' , font = ('Arial',18))
    generate_btn = Button(Top1,text = 'Generate ', font = ('Arial',17), fg = 'red' , command = generate)
    space = Label(Top1,text = '')
    space1 = Label(Top1,text = '')
    space2 = Label(Top1,text = '')
    pass_here = Label(Top1,text = '1' , font = ('Arial',16))
    heading_password.pack()
    generate_btn.pack()
    space.pack()
    space1.pack()
    space2.pack()
    pass_here.pack()


def open_text():
    os.system('editor.py')

def open_atm():
    os.system('atm.py')

def open_color():
    os.system('color.py')


def homepage():
    # DETROYING
    global password , start_pass,name,pass_heading
    password.destroy()
    start_pass.destroy()
    name.destroy()
    pass_heading.destroy()

    #MENU BARS 
    main_menu = Menu(root)
    root.config(menu = main_menu)
    file_menu = Menu(main_menu,tearoff = 0)
    main_menu.add_cascade(label = 'File',menu = file_menu)
    file_menu.add_command(label = 'New file')
    file_menu.add_command(label = 'Save')
    file_menu.add_command(label = 'Save as')
    file_menu.add_command(label = 'Open')
    file_menu.add_command(label = 'Exit',command = root.quit)

    edit_menu = Menu(main_menu,tearoff = 0)
    main_menu.add_cascade(label = 'Edit',menu = edit_menu)
    edit_menu.add_command(label = 'Font')
    edit_menu.add_command(label = 'Bold')
    edit_menu.add_command(label = 'Italic')

    help_menu = Menu(main_menu, tearoff = 0)
    main_menu.add_cascade(label = 'Help',menu = help_menu)
    help_menu.add_command(label = 'Info')
    help_menu.add_command(label = 'Bug')
    help_menu.add_command(label = 'Question with Chatbot ?')

    #WORK

    top = Frame(root)
    bottom = Frame(root)    
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
    space1 = Label(root,text ='')
    
    google_btn = Button(root,text='Password Generator',command = open_password , font = ('Arial',18),fg = 'red' )
    space_btn = Label(root,text = '')
    space_btn1 = Label(root,text = '')
    space_btn2 = Label(root,text = '')

    text_edtor_btn = Button(root,text = 'Text Editor',fg = 'blue',font = ('Arial',18),command = open_text)
    space_btn3 = Label(root,text = '')
    space_btn4 = Label(root,text = '')
    space_btn5 = Label(root,text = '')

    atm_btn = Button(root,text = 'ATM',font = ('Arial',18),command = open_atm)
    space_btn6 = Label(root,text = '')
    space_btn7 = Label(root,text = '')
    space_btn8 = Label(root,text = '')

    color_btn = Button(root,text = 'Color Game' , font = ('Arial' , 18) , command = open_color)
    space_btn9 = Label(root,text = '')
    space_btn10 = Label(root,text = '')
    space_btn11 = Label(root,text = '')

    google_btn.pack(in_=top, side=LEFT)
    space_btn.pack(in_=top, side=LEFT)
    space_btn1.pack(in_=top, side=LEFT)
    space_btn2.pack(in_=top, side=LEFT)

    text_edtor_btn.pack(in_=top, side=LEFT)
    space_btn3.pack(in_=top, side=LEFT)
    space_btn4.pack(in_=top, side=LEFT)
    space_btn5.pack(in_=top, side=LEFT)

    atm_btn.pack(in_=top, side=LEFT)
    space_btn6.pack(in_=top, side=LEFT)
    space_btn7.pack(in_=top, side=LEFT)
    space_btn8.pack(in_=top, side=LEFT)

    color_btn.pack(in_ = top , side = LEFT)
    space_btn9.pack(in_ = top , side = LEFT)
    space_btn10.pack(in_ = top , side = LEFT)
    space_btn11.pack(in_ = top , side = LEFT)

    # STATUS BAR
    global status_bar
    status_bar = Label(root,text = '', anchor = E , font = ('Arial',14))
    status_bar.pack(fill = X , side = TOP , ipady = 400)
    clock()







#Password
name = Label(root,text = 'Parshav Jain',font = ('Arial',18))
name.pack()
pass_heading = Label(root,text = 'Password : ')
pass_heading.pack()
password = Entry(root,width = 20,borderwidth = 10,show ='*',font = ('Arial',17))
password.pack()
start_pass = Button(root,text = 'Start',command = password_func) 
start_pass.pack()

root.bind('<Return>',password_func)


root.mainloop()

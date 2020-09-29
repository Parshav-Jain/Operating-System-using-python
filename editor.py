from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import font
root= Tk()
root.title('Text Editor')
root.resizable(0,0)

# FUNCTION
def bold():
    bold_font = font.Font(main , main.cget('font'))
    bold_font.configure(weight = 'bold')

    main.tag_configure('bold' , font = bold_font)
    current_tags = main.tag_names('sel.first')
    if 'bold' in current_tags:
        main.tag_remove('bold','sel.first','sel.last')
    else:
        main.tag_add('bold', 'sel.first','sel.last')
def italic():

    italic_font = font.Font(main , main.cget('font'))
    italic_font.configure(slant = 'italic')

    main.tag_configure('bold' , font = italic_font)
    current_tags1 = main.tag_names('sel.first')
    if 'italic' in current_tags1:
        main.tag_remove('italic','sel.first','sel.last')
    else:
        main.tag_add('italic', 'sel.first','sel.last')
    

def new():
    main.delete(1.0,END)
def open():
    main.delete(1.0,END)
    text_file = filedialog.askopenfilename(initialdir = 'Desktop',title = 'Open File',filetypes = (('Text Files' , '*.txt') , ('HTML files' , '*.html') , ('Python Files' , '*.py')))

    text_file = open(text_file , 'r')
    main.insert(END , stuff)
    text_file.close()

def color():
    global selected_text
    font_color = colorchooser.askcolor()[1]
    main.config(fg = font_color)
def fonts():
    def start_fonts():
        main.config(font = (stri.get() , inte.get() ))
    
    Top = Toplevel()
    inte = IntVar()
    stri = StringVar()
    font_size = OptionMenu(Top,inte,10,11,12,13,14,15,16,17,18,19,20)
    font_style = OptionMenu(Top,stri,'Times New Roman','Helvetica','Arial','Monospace','Cursive')
    inte.set(16)
    stri.set('Arial')
    font_size.pack()
    font_style.pack()

    start_btn_fonts = Button(Top,text = 'Save',command = start_fonts)
    start_btn_fonts.pack()

#MAIN 
my_frame = Frame(root)
my_frame.pack(pady = 5)
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT , fill = Y)


main = Text(my_frame,width = 100 , height = 20,font = ('Arial',14),selectbackground = 'yellow',selectforeground = 'black',undo = True,yscrollcommand = text_scroll.set)
main.pack()
text_scroll.config(command = main.yview)

staus_bar = Label(root,text = 'Text Editor', anchor = E)
staus_bar.pack(fill = X , side = BOTTOM , ipady = 5)


#MENU BAR
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label = 'File',menu = file_menu)
file_menu.add_command(label = 'New',command = new)
file_menu.add_command(label = 'Open',command = open)
file_menu.add_command(label = 'Save')
file_menu.add_command(label = 'Save as')
file_menu.add_command(label = 'Exit',command = root.quit)

edit_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label = 'Edit',menu = edit_menu)
edit_menu.add_command(label = 'Bold' , accelerator = 'Ctrl + B',command = bold)
edit_menu.add_command(label = 'Italic', accelerator = 'Ctrl + I',command = italic)
edit_menu.add_command(label = 'Color',command = color)
edit_menu.add_command(label = 'Font-Style',command = fonts)
edit_menu.add_command(label = 'Undo',command = main.edit_undo,accelerator = 'Ctrl + Z')
edit_menu.add_command(label = 'Redo',command = main.edit_redo,accelerator = 'Ctrl + Y')

help_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label = 'Help',menu = help_menu)
help_menu.add_command(label = 'Info')
help_menu.add_command(label = 'Bug')
help_menu.add_command(label = 'Question With Chatbot ? ')

root.mainloop()

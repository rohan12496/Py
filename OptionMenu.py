from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk


t = Tk()
t.geometry('1000x700+0+0')

options = ['Sales Invoice','Customer','Purchase Invoice','Supplier','Company','Customize']

def select(event):
    t1 = Tk()
    t1.geometry('1000x500+0+0')

    Label(t1,text=hr.get()).pack()

    t1.mainloop()

getting_started = StringVar()
accounting = StringVar()
selling = StringVar()
buying = StringVar()
stock = StringVar()
assets = StringVar()
projects = StringVar()
crm = StringVar()
support = StringVar()
hr = StringVar()
quality = StringVar()

getting_started.set('Getting Started')        # set the default option
accounting.set('Accounting')
selling.set('Selling')
buying.set('Buying')
stock.set('Stock')
assets.set('Assets')
projects.set('Projects')
crm.set('CRM')
support.set('Support')
hr.set('Human Resources')
quality.set('Quality')

lbl_module = Label(t,text='MODULES',font=('arial',12,'bold'),fg='gray55')
lbl_module.pack(padx=10,pady=10,anchor=W)

'''menu = OptionMenu(t,click,*options,command=select)
menu.pack()'''

module_frame = Frame(t)
module_frame.place(y=50,height=300,width=1000)

'''menu = OptionMenu(module_frame,getting_started,*options,command=select)
menu['width']=40
menu['height']=2
menu.grid(row=0,column=0,padx=10,pady=10)'''

img = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop1.png'))
menu = OptionMenu(module_frame,getting_started,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img)
menu.grid(row=0,column=0,padx=10,pady=10)

img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop2.png'))
menu = OptionMenu(module_frame,accounting,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img2)
menu.grid(row=0,column=1,padx=10,pady=10)

img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop3.png'))
menu = OptionMenu(module_frame,selling,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img3)
menu.grid(row=0,column=2,padx=10,pady=10)

img4 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop4.png'))
menu = OptionMenu(module_frame,buying,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img4)
menu.grid(row=1,column=0,padx=10,pady=10)

img5 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop5.png'))
menu = OptionMenu(module_frame,stock,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img5)
menu.grid(row=1,column=1,padx=10,pady=10)

img6 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop6.png'))
menu = OptionMenu(module_frame,assets,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img6)
menu.grid(row=1,column=2,padx=10,pady=10)

img7 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop7.png'))
menu = OptionMenu(module_frame,projects,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img7)
menu.grid(row=2,column=0,padx=10,pady=10)

img8 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop8.png'))
menu = OptionMenu(module_frame,crm,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img8)
menu.grid(row=2,column=1,padx=10,pady=10)

img9 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop1.png'))
menu = OptionMenu(module_frame,support,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img9)
menu.grid(row=2,column=2,padx=10,pady=10)

img10 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop9.png'))
menu = OptionMenu(module_frame,hr,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img10)
menu.grid(row=3,column=0,padx=10,pady=10)

img11 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop1.png'))
menu = OptionMenu(module_frame,quality,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img11)
menu.grid(row=3,column=1,padx=10,pady=10)

lbl_domains = Label(t,text='DOMAINS',font=('arial',12,'bold'),fg='gray55')
lbl_domains.place(x=10,y=380,anchor=W)

domains = StringVar()
domains.set('Domains')

domain_frame = Frame(t)
domain_frame.place(y=400,height=80,width=900)

img12 = ImageTk.PhotoImage(Image.open(r'C:\Users\rohan\Downloads\Documents\desktop10.png'))
menu = OptionMenu(domain_frame,quality,*options,command=select)
menu['width']=240
menu['height']=30
menu.config(compound='left',image=img12)
menu.grid(row=0,column=0,padx=10,pady=10)

t.mainloop()


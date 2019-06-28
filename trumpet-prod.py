from barcode import generate
from tkinter import *
import os
from barcode.writer import ImageWriter
from PIL import Image
import json


class Trumpet(object):
    def __init__(self, tr_name, label_name, barcode):
        self.tr_name = tr_name
        self.label_name = label_name
        self.barcode = barcode

    def create(self, event, metr):
        if int(metr) > 0:
            label_text = '{} {}М'.format(self.label_name, metr)
            name = generate('EAN13', self.barcode, output='barcode',
                            text=label_text, writer=ImageWriter())  # writer.py 325
            im = Image.open("barcode.png")
            pdf_file = "barcode.pdf"
            im.save(pdf_file, "PDF", resolution=100.0)
            os.startfile("barcode.pdf", "print")
            text.set('')

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['tr_name'], js_object['label_name'], js_object['barcode'])

    def __repr__(self):
        return 'Trumpet({!r}, {!r}, {!r})'.format(self.tr_name, self.label_name, self.barcode)


def enter(event, num):
    metres = '{}{}'.format(text.get(), num)
    text.set(metres)


def sbros(event):
    text.set('')

label_manual = '''
	1.Введи количество отрезного товара 
	2.Выбери нужный товар 
	3.Забери этикетку'''

try:
	with open('data/trumpet.json', 'r', encoding="utf8") as file:
		trumpetss = json.load(file, object_hook=Trumpet.from_json)
except Exception as e:
	label_manual = "База повреждена!"
	trumpets = []
else:
	trumpets = trumpetss

    

root = Tk()
root.title('Trumpet')
root.wm_attributes('-topmost', 1)
root.overrideredirect(1)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                   root.winfo_screenheight()))
root.resizable(False, False)

text = StringVar()
text.set('')


trumpetFrame = Frame(root, bg="white", width=50)
inputFrame = Frame(root, bg="white")

trumpetFrame.pack(side='left', fill='both', expand=0)
inputFrame.pack(side='right', fill='both', expand=1)

metres = Entry(inputFrame, width=7, textvariable=text,
               font="Helvetica 44 bold", fg="black", bd=5)
metres.pack(side='top', fill='none', expand=0)



manual = Label(inputFrame, text=label_manual, bg='white', justify='left',font="Helvetica 14")
manual.pack(side='top', fill='both', expand=0)

firstline = Frame(inputFrame, height=10)
secondline = Frame(inputFrame, height=10)
thirdline = Frame(inputFrame, height=10)
zeroline = Frame(inputFrame, height=10)

firstline.pack(side='top', fill='y', expand=0)
secondline.pack(side='top', fill='y', expand=0)
thirdline.pack(side='top', fill='y', expand=0)
zeroline.pack(side='top', fill='y', expand=0)

# NUM-PAD
# *************************************************************
but1 = Button(firstline, text="1", width=10, height=5, bg="white", fg="black")
but1.pack(side='left', fill='none')
but1.bind("<Button-1>", lambda event: enter(event, 1))

but2 = Button(firstline, text="2", width=10, height=5, bg="white", fg="black")
but2.pack(side='left', fill='none')
but2.bind("<Button-1>", lambda event: enter(event, 2))

but3 = Button(firstline, text="3", width=10, height=5, bg="white", fg="black")
but3.pack(side='left', fill='none')
but3.bind("<Button-1>", lambda event: enter(event, 3))

but4 = Button(secondline, text="4", width=10, height=5, bg="white", fg="black")
but4.pack(side='left', fill='none')
but4.bind("<Button-1>", lambda event: enter(event, 4))

but5 = Button(secondline, text="5", width=10, height=5, bg="white", fg="black")
but5.pack(side='left', fill='none')
but5.bind("<Button-1>", lambda event: enter(event, 5))

but6 = Button(secondline, text="6", width=10, height=5, bg="white", fg="black")
but6.pack(side='left', fill='none')
but6.bind("<Button-1>", lambda event: enter(event, 6))

but7 = Button(thirdline, text="7", width=10, height=5, bg="white", fg="black")
but7.pack(side='left', fill='none')
but7.bind("<Button-1>", lambda event: enter(event, 7))

but8 = Button(thirdline, text="8", width=10, height=5, bg="white", fg="black")
but8.pack(side='left', fill='none')
but8.bind("<Button-1>", lambda event: enter(event, 8))

but9 = Button(thirdline, text="9", width=10, height=5, bg="white", fg="black")
but9.pack(side='left', fill='none')
but9.bind("<Button-1>", lambda event: enter(event, 9))

but0 = Button(zeroline, text="0", width=10, height=5, bg="white", fg="black")
but0.pack(side='left', fill='none')
but0.bind("<Button-1>", lambda event: enter(event, 0))

metres_sbros = Button(zeroline, text="Сбросить", width=10,
                      height=5, bg="white", fg="black")
metres_sbros.pack(side='right', fill='none')
metres_sbros.bind("<Button-1>", sbros)

# ВЫБОР ТОВАРА
# *************************************************************

trumpet_but = []
for i in range(0, len(trumpets)):
    if i < 12:  # len(trumpets)/2:
        trumpet_but.append(Button(
        trumpetFrame, text=trumpets[i].tr_name, width=50, height=4, bg="white", fg="black"))
    elif i == 12:
        trumpetFrame2 = Frame(root, bg="white", width=50)
        trumpetFrame2.pack(side='left', fill='both', expand=0)
        trumpet_but.append(Button(
            trumpetFrame2, text=trumpets[i].tr_name, width=50, height=4, bg="white", fg="black"))
    elif i < 24:
        trumpet_but.append(Button(
            trumpetFrame2, text=trumpets[i].tr_name, width=50, height=4, bg="white", fg="black"))
    elif i == 24:
        trumpetFrame3 = Frame(root, bg="white", width=50)
        trumpetFrame3.pack(side='left', fill='both', expand=0)
        trumpet_but.append(Button(
            trumpetFrame3, text=trumpets[i].tr_name, width=50, height=4, bg="white", fg="black"))
    else:
        trumpet_but.append(Button(
        trumpetFrame3, text=trumpets[i].tr_name, width=50, height=4, bg="white", fg="black"))
    trumpet_but[i].pack(side='top', fill='none', expand=1)
    trumpet_but[i].bind(
        "<Button-1>", lambda event, i=i: trumpets[i].create(event, text.get()))

logo = PhotoImage(file = 'LM.png')
lm = Label(inputFrame, image=logo, bg='white', width = 400)
lm.pack(side='bottom')



root.mainloop()

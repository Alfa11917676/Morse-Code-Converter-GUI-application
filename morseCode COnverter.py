from tkinter import *
from functools import partial
import tkinter.messagebox as tmessage
win=Tk()
codes = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
}

#Save Confirmation Function
def foolFunction():
    show=tmessage.showinfo("Confirmation","Your File Is Saved In Your Device in the name of %s"%x)



#Random name is taken to save the files with Differnet name
from random import choice

name = ["one", "two", "three", "foure", "five", "sixerer", "dosfho", "ishfak", "momin", "ali", "chand", "gazal",
        "python", "tkihnter", "label"]
x = choice(name)

#Auto Save Function Is Being Performed
def saveFunction(something,some):

    newFile=open("%s.txt"%x,"w")
    text=something+"="+some
    newFile.write(text)
#MorseCode To Text
def sssum(label,x2):
    n2 = (x2.get())
    word=n2

    word += ' '

    decipher = ''
    citext = ''
    for letter in word:

        if (letter != ' '):


            i = 0

            citext += letter

        else:

            i += 1


            if i == 2:


                decipher += ' '
            else:

                decipher += list(codes.keys())[
                    list(codes.values()).index(citext)]
                citext = ''
    label.config(text=decipher)
    saveFunction(word,decipher)
    return decipher

#Text to MorseCode Converter Function
def sum(label,x1):
    n1=(x1.get())


    code = n1
    word = code.upper()
    a = ""
    for i in word:

        if (i !=" "):
            a += codes[i]+" "
        else:
            a += " "

    label.config(text=a)
    saveFunction(word,a)
    return a

#GUI Building
l0=Label(win,text="Welcome to the MorseCode Converter",fg="BLue",bg="Violet" )
l0.grid(row=2,column=2)
l1=Label(win,text="Enter the text to be encrypted:  ",fg="BLue",bg="Violet")
l1.grid(row=3,column=0)
l2=Label(win,text="Enter the MorseCode to be decyphyered:  ",fg="BLue",bg="Violet")
l2.grid(row=5,column=0)
label =Label(win)
win.geometry("550x100")
label.grid(row=6,column=2)
x1=StringVar()
x2=StringVar()
e1=Entry(win,textvariable=x1)
e2=Entry(win,textvariable=x2)

win.title("MORSECODE CONVERTER")
e1.grid(row=3,column=2)
e2.grid(row=5,column=2)
win.configure(background="Blue")
sum=partial(sum,label,x1)

#Button Is Decleared
button=Button(win,text="Encrypt",command=sum,fg="BLue",bg="Violet")
sssum=partial(sssum,label,x2)
button2=Button(win,text="Decrypt",command=sssum,fg="BLue",bg="Violet")
button2.grid(row=5,column=3)

button.grid(row=3,column=3)
#MenuBar Layout Design
mymenu=Menu(win)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="Save",command=foolFunction)
m1.add_command(label="Exit",command=quit)
m1.add_separator()
win.config(menu=mymenu)
mymenu.add_cascade(label="File",menu=m1)
#Last Packing Of the GUI LAyout
win.mainloop()
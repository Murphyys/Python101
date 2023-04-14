from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
GUI = Tk()  #this is main phrase
GUI.title('saving program') #this program'name
GUI.geometry('500x400')

def but1():
    text= 'ออกกำลังกาย'
    messagebox.showinfo('สิ่งที่ทำ',text)

B1= ttk.Button(GUI,text='show your money',command=but1)
B1.pack()

B2= Button(GUI,text='show your money')
B2.pack()

GUI.mainloop()

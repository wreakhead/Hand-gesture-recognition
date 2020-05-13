from tkinter import *  
import sys
import os
top=Tk()
top.title("gesture control")
#top.geometry("500x500")
top.configure(background="black")
photo = PhotoImage(file="ABC.png")
photo1 = PhotoImage(file="word.png")

def gesturealfa():
    os.system('readalfa.py')
def gestureword():
    os.system('readword.py')

disp=Label(top, text="Select Type:",bg="black",fg="light blue")        

alfabutton = Button(top,image=photo,command=gesturealfa,relief="flat",activebackground="grey",bg="black")#text="Alfa"padx="30",pady="25",
blank1 = Button(top,text="",padx="10",pady="25",state="disabled",bg="grey",relief="flat")
wordbutton = Button(top,image=photo1,command=gestureword,relief="flat",activebackground="grey",bg="black")

exitbutton=Button(top,text='Quit',command=top.quit,bg="black",fg="light blue",relief="flat")

exitbutton.grid(row=3,column=1)
alfabutton.grid(row=1,column=0)
blank1.grid(row=1,column=1)
wordbutton.grid(row=1,column=2)
disp.grid(row=0,column=1)
top.mainloop()

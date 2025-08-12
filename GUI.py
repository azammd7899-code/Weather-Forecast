import tkinter
from cProfile import label
from tkinter import *
from tkinter import messagebox
import webbrowser
import  subprocess


def web():
    messagebox.showinfo('web','website will open')
    webbrowser.open('https://www.bietdvg.edu/')

def pro():
       messagebox.showinfo('pro', 'project will open')
       cmd='Python weather.py'
       p=subprocess.Popen(cmd,shell=True)
def rep():
    messagebox.showinfo('REPORT','REPORT will open')
    webbrowser.open('intern rep.pdf')

def ppt():
    messagebox.showinfo('ppt','ppt will open')
    webbrowser.open('new1 Weather_forcat_Edition.pptx')

def G():
    messagebox.showinfo('G','GIDE will open')
    webbrowser.open('guid res.pdf')

def MY():
    messagebox.showinfo('MY','MY RESUME will open')
    webbrowser.open('My resume.pdf')

gui=Tk()
gui.geometry('600x485')
gui.title('LOAN ')
gui.config(bg='grey')

BG=PhotoImage(file='GUIPICS/bag.png')
BGL=Label(image=BG).place(x=0,y=127)
LabelFrame=Label(text='WEATHER FORCAST').place(x=242,y=130)

LOGO=PhotoImage(file='GUIPICS/LOGO.png')
LOGOb=Button(gui,image=LOGO,command=web).place(x=3,y=0)

PRO=PhotoImage(file='GUIPICS/logo pro.png')
PROb=Button(gui,image=PRO,command=pro).place(x=50,y=160)
PROL=Label(text='PROJECT').place(x=76,y=269)

REP=PhotoImage(file='GUIPICS/report.png')
REPb=Button(gui,image=REP,command=rep).place(x=250,y=158)
REPL=Label(text='REPORT').place(x=280,y=267)


PPT=PhotoImage(file='GUIPICS/ppt.png')
PPTb=Button(gui,image=PPT,command=ppt).place(x=450,y=160)
PPTL=Label(text='PRESENTATION').place(x=458,y=268)

STUDENT=PhotoImage(file='GUIPICS/azam.png')
STUDENTB=Button(gui,image=STUDENT,command=MY).place(x=100,y=300)
STUL=Label(text='STUDENT').place(x=120,y=434)
STUL2=Label(text='MOHAMMED AZAM').place(x=90,y=456)

GUIDE=PhotoImage(file='GUIPICS/GUIDE.png')
GUIDEB=Button(gui,image=GUIDE,command=G).place(x=390,y=300)
GUI=Label(text='GUIDE').place(x=420,y=430)
GUI2=Label(text='ROOPA R').place(x=411,y=453)

gui.mainloop()
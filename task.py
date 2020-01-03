from tkinter import *
from utils import *
from threading import Thread
import time


class AnsTimer(Thread):
    def __init__(self, time_display):
        Thread.__init__(self)
        self.time_display=time_display
    def run(self):
        global seconds
        global cont
        while True:
            if cont:
                while seconds >=0:
                    self.time_display['text']=seconds
                    time.sleep(1)
                    seconds-=1
                cont=False
                show_score(master, score)
def submit():
    global level
    global score
    global cont
    global img
    global seconds
        
    propo=e1.get()
    statut=check_img(img, propo)
    if statut:
        cont=False
        score=score*level+2
        score_label['text']='Score: '+str(score)
        level+=1
        master.title("Geek GCI Level: "+str(level))
        img=choose_img(can1, level)
        seconds=11
        cont=True
    else:
        if score>0:
            score-=1
        master.title("Geek GCI Level: "+str(level))
        hint=get_hint(img)
        hint_label['text']=hint
        seconds=11
        cont=True

level=1
score=0

master = Tk()
master['bg']="green"
master.resizable(False, False)
master.protocol("WM_DELETE_WINDOW", lambda master=master:quit_master(master))
master.title("Geek GCI")

name = StringVar()

Label(master, text='WildCard Game', width=50, bg='green', fg="yellow", relief="raised").grid(column=0, columnspan=2)
time_label=Label(master, text='10s', width=25, bg='green', fg="yellow", relief="raised")
time_label.grid(row=1)
score_label=Label(master, text='Score: '+str(score), width=25, bg='green', fg="yellow", relief="raised")
score_label.grid(row=1, column=1)

can1 = Label(master, width = 250, height = 300, bg = 'white')
can1.grid(row=2, rowspan=5, column=0, columnspan=2)


hint_label=Label(master, text='???????? Hint ????????', width=50, bg='green', fg="yellow", relief="raised")
hint_label.grid(row=7, column=0, columnspan=2)
Label(master, text='Name: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=8)
e1 = Entry(master, width=25, textvariable=name)
e1.grid(row=8, column=1)


img=choose_img(can1, level)
seconds=10
cont=True
t=AnsTimer(time_label)
t.start()
Button(master, width=25, text="Go!!", bg='green', fg="yellow", relief="raised", command=submit).grid(row=9, column=0, columnspan=2)

master.mainloop()

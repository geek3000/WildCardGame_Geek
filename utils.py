from PIL import Image, ImageTk
import os, random, pickle, sys
from tkinter.messagebox import askokcancel
import tkinter as tk


index_img=0
img_level=0
img_name={}
def quit_master(master):
    if askokcancel("Quit", "Do you really wish to quit this game?"):
        master.destroy()
        sys.exit(0)
def quit_win(master):
    master.destroy()
    sys.exit(0)
    
def show_score(master, score):
    win=tk.Toplevel(master)
    win['bg']="green"
    win.resizable(False, False)
    win.protocol("WM_DELETE_WINDOW", lambda master=master:quit_win(master))
    image=charger_image("./img/score.png")
    sc_image=tk.Label(win, bg='green', fg="yellow", relief="raised", image=image)
    sc_image.image=image
    sc_image.pack()
    sc_label=tk.Label(win, bg='green', fg="yellow", relief="raised", width=35, text="Votre score est: "+str(score))
    sc_label.pack()
    tk.Button(win, text="OK", bg='yellow', fg="green", relief="raised", width=35, command=lambda master=master:quit_win(master)).pack()

def charger_image(filename):
    img = Image.open(filename)
 
    photo = ImageTk.PhotoImage(img)
    return photo

def choose_img(can, level):

    
    path="./img/l"+str(level)
    img_list=os.listdir(path)
    img=random.choice(img_list)
    img_path=path+'/'+img
    
    image=charger_image(img_path)
    can['image']=image
    can.image=image
    
    return img.split('.')[0]

def check_img(img, name):
    img_names=pickle.load(open('data.word', 'rb'))
    try:
        names=img_names[img+'.jpg']
    except:
        names=img_names[img+'.png']
    if name.lower() in names:
        return True
    else:
        return False

def get_hint(img):
    hints=pickle.load(open('hint.word', 'rb'))
    try:
        hint=hints[img+'.jpg']
    except:
        hint=hints[img+'.png']
    return hint

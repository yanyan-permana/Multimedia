from tkinter import *
from tkinter import filedialog
from turtle import st
from pygame import mixer

root = Tk()
root.title('Pemutar Musik Menggunakan Pyhton')
root.config(background='lightyellow')

mixer.init()
Label(root, text='Pemutar Musik MP3', bg='lightyellow',
      font='Normal 40').grid(row=0, column=0, columnspan=3, pady=10)

# Cari musik


def carimusic():
    file = filedialog.askopenfilename(filetypes=[('mp3', '*.mp3')])
    if file == "":
        return
    mixer.music.load(file)
    t.config(state=NORMAL)
    t.delete(1.0, END)
    t.insert(END, file)
    t.config(state=DISABLED)


b = Button(root, text='Cari Musik', font='Normal 25',
           command=carimusic, relief=RIDGE, bd=10, activebackground='lightblue')
b.grid(row=1, column=1, ipadx=30, pady=5)

t = Text(root, font='Normal 15', background='lightyellow',
         wrap=WORD, height=3, width=50)

t.grid(row=2, columnspan=3, pady=15)
t.config(state=DISABLED)

# Pause


def pause():
    mixer.music.pause()


b1 = Button(root, text='Pause', font='Normal 25', command=pause,
            relief=RIDGE, bd=10, activebackground='lightblue')
b1.grid(row=3, column=0, padx=15, ipadx=15)

# Mainkan


def play():
    mixer.music.play(-1)


b2 = Button(root, text='Mainkan', font='Normal 25', command=play,
            relief=RIDGE, bd=10, activebackground='lightblue')
b2.grid(row=3, column=1, padx=10)

# Unpause


def unpause():
    mixer.music.unpause()


b3 = Button(root, text='Unpause', font='Normal 25', command=unpause,
            relief=RIDGE, bd=10, activebackground='lightblue')
b3.grid(row=3, column=2, padx=10)

# Berhanti


def stop():
    mixer.music.stop()


b4 = Button(root, text='Berhenti', font='Normal 25', command=stop,
            relief=RIDGE, bd=10, activebackground='lightblue')
b4.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()

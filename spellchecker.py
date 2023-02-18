import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk ()
root.title('spelling checker')
root.geometry('650x400')
root.config(background = '#CDE990')

def check_spelling():
    word = enter_text.get()
    a = TextBlob (word)
    right = str(a.correct())
    
    cs = Label(root, text = 'correct spelling:', font=('Old Soviet', 12), fg = '#FFFFE8', bg = '#CDE990')
    cs.place (x=185, y=230)
    spell.config(text=right)

heading = Label(root, text = 'spelling checker', font = ('Old Soviet', 22), bg = '#CDE990', fg = '#FFFFE8')
heading.pack(pady= (35,0))

enter_text = Entry(root, justify='center', width=30, font=('Old Soviet', 12), bg='#FFFFE8', fg='#AACB73', border=0)
enter_text.configure(insertbackground='#CDE990')
enter_text.pack(pady=(35,0))
enter_text.focus()

the_button=Button(root, text='CHECK', font=('Old Soviet', 12), justify='center', fg = '#FFFFE8', bg='#FFAACF', border=0, command=check_spelling)
the_button.pack(pady=35)

spell = Label(root, font=('Old Soviet', 12), fg = '#FFFFE8', bg = '#CDE990')
spell.place(x=350, y=230)

root.mainloop()
from tkinter import *
from tkinter import messagebox
import random

root = Tk()

list = ['Да', 'Нет', 'Не знаю', 'Может быть', 'Возможно',
        'Абсолютно точно','Даже не думай','Скорее всего нет',
        'Спроси позже','Никаких сомнений']

def set_value(formula: object) -> object:
    if formula == '':
        lbl['text']=''
    else:
        lbl['text'] = random.choice(list)


def button_1(choice):
	a = random.choice(list)
    if choice == a:
        set_value(lbl[a])


root.resizable(False, False)

root.title('Рандомайзер')
root.geometry('250x250')
root["bg"] = "black"

x = 70
y = 140

lbl = Label(font=("Consolas", 21, "bold"), text = random.choice(dict), bg="blue", foreground="white")
lbl.place(x=55, y=20, width = 150, height = 70)

button = Button(text='Рандомный выбор', fg = 'white', bg = 'black', activebackground = 'blue', command = button_1)
button.place(x=x, y=y, width=115,  heigh=79)

root.mainloop()

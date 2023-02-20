from tkinter import *
from tkinter import messagebox
import random

root = Tk()

dict = ['Да', 'Нет', 'Не знаю']

def button_1():
	a = random.choice(dict)
	messagebox.showinfo('', a)

root.title('Приложение')
root.geometry('500x200')
Button(text='Рандомный выбор', fg = 'red', activebackground = 'cyan', command = button_1).pack()

root.mainloop()

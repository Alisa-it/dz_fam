from tkinter import *
from tkinter import ttk
from graphs import define_lst

root = Tk()
root.configure(bg='white')

label = ttk.Label(root, text='Вариант №', background='white', font=('Arial', 12, 'bold'))
label.grid(row=0, column=0, pady=10, padx=20)

entry = ttk.Entry(root, font=('Arial', 12))
entry.grid(row=0, column=1, pady=10, padx=20)


def get_entry_value():
    value = entry.get()
    define_lst(int(value))
    root.destroy()

style = ttk.Style()
button = ttk.Button(root, text="Рассчитать", width=15, command=get_entry_value)
button.grid(row=1, column=1, pady=25, padx=20, sticky='se')
style.configure('TButton', height=10, padding=[5,5,5,5], font=('Arial', 12, 'bold'))
style.map('TButton')

root.mainloop()

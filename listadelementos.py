import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 3)
label1 = ttk.Label(window, text= "Lista de compras")
label1.grid(column = 0, row=0, sticky= tkinter.W, padx=5, pady=5 )

lista=['Harina','Leche','Huevo','Queso','Mantequilla','lechuga','tomate','papel higienico','cebolla','Pan']
lista_compras = tkinter.StringVar(value = lista)

listbox = tkinter.Listbox(window, height=20, listvariable= lista_compras)
listbox.grid(column=0,row=1,sticky= tkinter.W)

window.mainloop()
sys.exit(0)
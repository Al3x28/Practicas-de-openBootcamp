import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

def Resetear (event):
    selecionado.set('0')

window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 3)

label1 = ttk.Label(window, text= "Que color prefieres: ")
label1.grid(column = 0, row=0, sticky= tkinter.W, padx=5, pady=5 )

selecionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text= 'Azul', value= '1', variable= selecionado)
r2 = ttk.Radiobutton(window, text= 'Rojo', value= '2', variable= selecionado)
r3 = ttk.Radiobutton(window, text= 'Amarillo', value= '3', variable= selecionado)
r4 = ttk.Radiobutton(window, text= 'Verde', value= '4', variable= selecionado)

r1.grid(column = 0, row=1, sticky= tkinter.W, padx=5, pady=5 )
r2.grid(column = 0, row=2, sticky= tkinter.W, padx=5, pady=5 )
r3.grid(column = 0, row=3, sticky= tkinter.W, padx=5, pady=5 )
r4.grid(column = 0, row=4, sticky= tkinter.W, padx=5, pady=5 )

button= tkinter.Button(window, text= 'Reset' )
button.grid(column = 1, row=5, sticky= tkinter.W, padx=5, pady=5 )

button.bind('<Button-1>', Resetear)

window.mainloop()
sys.exit(0)


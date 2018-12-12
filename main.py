#!/usr/bin/env python3

from math import *
from tkinter import *

class Calculator:

    def __init__(self):
        self._welcome = "Here is basic calculator program please choose what you want to do"


    def addition(nb1, nb2):
        result = nb1 + nb2
        print(result)


# nb 1 = input(number 1 :)
# func = input(operation :)
# nb 1 = input(number 1 :)
fenetre = Tk()
Button(fenetre, text='x ²', borderwidth=1).grid(row=0, column=1, sticky=S+N+W+E)
Button(fenetre, text='x^y', borderwidth=1).grid(row=0, column=2, sticky=S+N+W+E)
Button(fenetre, text='sin', borderwidth=1).grid(row=0, column=3, sticky=S+N+W+E)
Button(fenetre, text='cos', borderwidth=1).grid(row=0, column=4, sticky=S+N+W+E)
Button(fenetre, text='tan', borderwidth=1).grid(row=0, column=5, sticky=S+N+W+E)
Button(fenetre, text='sqr', borderwidth=1).grid(row=1, column=1, sticky=S+N+W+E)
Button(fenetre, text='10^', borderwidth=1).grid(row=1, column=2, sticky=S+N+W+E)
Button(fenetre, text='log', borderwidth=1).grid(row=1, column=3, sticky=S+N+W+E)
Button(fenetre, text='Exp', borderwidth=1).grid(row=1, column=4, sticky=S+N+W+E)
Button(fenetre, text=' % ', borderwidth=1).grid(row=1, column=5, sticky=S+N+W+E)
Button(fenetre, text='   ', borderwidth=1).grid(row=2, column=1, sticky=S+N+W+E)
Button(fenetre, text='CE ', borderwidth=1).grid(row=2, column=2, sticky=S+N+W+E)
Button(fenetre, text='C  ', borderwidth=1).grid(row=2, column=3, sticky=S+N+W+E)
Button(fenetre, text='<--', borderwidth=1).grid(row=2, column=4, sticky=S+N+W+E)
Button(fenetre, text='/  ', borderwidth=1).grid(row=2, column=5, sticky=S+N+W+E)
Button(fenetre, text='pi ', borderwidth=1).grid(row=3, column=1, sticky=S+N+W+E)
Button(fenetre, text=' 7 ', borderwidth=1).grid(row=3, column=2, sticky=S+N+W+E)
Button(fenetre, text=' 8 ', borderwidth=1).grid(row=3, column=3, sticky=S+N+W+E)
Button(fenetre, text=' 9 ', borderwidth=1).grid(row=3, column=4, sticky=S+N+W+E)
Button(fenetre, text=' X ', borderwidth=1).grid(row=3, column=5, sticky=S+N+W+E)
Button(fenetre, text=' n!', borderwidth=1).grid(row=4, column=1, sticky=S+N+W+E)
Button(fenetre, text=' 4 ', borderwidth=1).grid(row=4, column=2, sticky=S+N+W+E)
Button(fenetre, text=' 5 ', borderwidth=1).grid(row=4, column=3, sticky=S+N+W+E)
Button(fenetre, text=' 6 ', borderwidth=1).grid(row=4, column=4, sticky=S+N+W+E)
Button(fenetre, text=' - ', borderwidth=1).grid(row=4, column=5, sticky=S+N+W+E)
Button(fenetre, text='+/-', borderwidth=1).grid(row=5, column=1, sticky=S+N+W+E)
Button(fenetre, text=' 1 ', borderwidth=1).grid(row=5, column=2, sticky=S+N+W+E)
Button(fenetre, text=' 2 ', borderwidth=1).grid(row=5, column=3, sticky=S+N+W+E)
Button(fenetre, text=' 3 ', borderwidth=1).grid(row=5, column=4, sticky=S+N+W+E)
Button(fenetre, text=' + ', borderwidth=1).grid(row=5, column=5, sticky=S+N+W+E)
Button(fenetre, text=' ( ', borderwidth=1).grid(row=6, column=1, sticky=S+N+W+E)
Button(fenetre, text=' ) ', borderwidth=1).grid(row=6, column=2, sticky=S+N+W+E)
Button(fenetre, text=' 0 ', borderwidth=1).grid(row=6, column=3, sticky=S+N+W+E)
Button(fenetre, text=' . ', borderwidth=1).grid(row=6, column=4, sticky=S+N+W+E)
Button(fenetre, text=' = ', borderwidth=1).grid(row=6, column=5, sticky=S+N+W+E)
value = StringVar() 
value.set("")
entree = Entry(fenetre, textvariable=value, width=30)
entree.grid(row=0, column = 6)
entree.pack
fenetre.mainloop()

from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

def m2py(fom):
	fom = fom.replace("^","**")
	fom = fom.replace("sin","np.sin")
	fom = fom.replace("cos","np.cos")
	fom = fom.replace("tan","np.tan")
	fom = fom.replace("pi","np.pi")
	fom = fom.replace("e","np.e")
	return fom


def graph():								# Graphs the function
	formula = m2py(str(eqnERY.get()))
	x = np.arange(eval(x_minERY.get()),eval(x_maxERY.get()),0.01)
	y = eval(formula)
	ax = plt.gca()
	ax.set_ylim([eval(y_minERY.get()),eval(y_maxERY.get())])
	
	plt.axhline(linewidth=2, y=0, color='black')
	plt.axvline(linewidth=2, x=0, color='black')

	if 'x' not in formula:
		plt.axhline(y=eval(formula))
	else:
		utol = 100.
		ltol = -100.
		y[y>utol] = np.inf
		y[y<ltol] = -np.inf 
		plt.plot(x,y)
	
	plt.grid(linestyle="--")
	plt.show()

def useDefault():							# Fills default values for the domain and range
	x_minERY.delete(0,END)
	x_maxERY.delete(0,END)
	y_minERY.delete(0,END)
	y_maxERY.delete(0,END)

	x_minERY.insert(0,-10)
	x_maxERY.insert(0,10)
	y_minERY.insert(0,-10)
	y_maxERY.insert(0,10)

root = Tk()
root.title("Graphing Calculator")
root.option_add("*Font", "courier 36")
root.resizable(False, False)

style = ttk.Style() 
style.configure('TButton', font = ('courier', 28, 'bold'))

eqnLBL = ttk.Label(root,text="y =")
eqnERY = ttk.Entry(root)

defaultBTN = ttk.Button(root, text="Use Default Limits", command=useDefault)

x_minLBL = ttk.Label(root, text="x min:")
x_minERY = ttk.Entry(root, width=5)

x_maxLBL = ttk.Label(root, text="x max:")
x_maxERY = ttk.Entry(root, width=5)

y_minLBL = ttk.Label(root, text="y min:")
y_minERY = ttk.Entry(root, width=5)

y_maxLBL = ttk.Label(root, text="y max:")
y_maxERY = ttk.Entry(root, width=5)

button = ttk.Button(root, text="PLOT", style="TButton", command=graph)

# Place all widgets on the grid

eqnLBL.grid(row=1,column=0, pady=10)
eqnERY.grid(row=1,column=1, pady=10)
defaultBTN.grid(row=0, column=0, columnspan=2, sticky=N, pady=(0,15))
button.grid(row=6,column=0, columnspan=2,sticky=N+S+W+E, pady=(30,0))

x_minLBL.grid(row=2,column=0, pady=10)
x_minERY.grid(row=2,column=1, sticky=W, pady=10)

x_maxLBL.grid(row=3,column=0, pady=10)
x_maxERY.grid(row=3,column=1, sticky=W, pady=10)

y_minLBL.grid(row=4,column=0, pady=10)
y_minERY.grid(row=4,column=1, sticky=W, pady=10)

y_maxLBL.grid(row=5,column=0, pady=10)
y_maxERY.grid(row=5,column=1, sticky=W, pady=10)

root.mainloop()
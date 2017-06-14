#This program makes a simple calculator that can add, subtract, multiply and divide

from tkinter import *
from tkinter import ttk

class Calculator(master):
	def __init__(self, master):
		self.master = master
		master.wm_title('Calculator')
		master.geometry('400x500')
		mainframe.grid(column=0,row=0,sticky=(N, W, E, S)
		mainframe.columnconfigure(0, weight=1)
		e = ttk.Entry(master, width=20)

if __name__ == "__main__":
	root = tk.Tk()
	calc = Calculator(root)
	root.mainloop()

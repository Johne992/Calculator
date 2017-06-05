#This program makes a simple calculator that can add, subtract, multiply and divide

import math
from tkinter import *

class Calculator(object):
	
	def __init__(self,master):
		master.title('Calculator')
		master.geometry()
		self.e = Entry(master)
		self.e.grid(row=0,column=0,columnspan=6,pady=3)
		self.e.focus_set()
		
		self.div='÷'
		self.newdiv = self.div.decode('utf-8')
		
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		pass
	
	#Adds two numbers
	def add(self,x, y):
		return x + y;
	
	#Subtract two integers
	def subtract(self,x, y):
		return x - y;
	
	#multiply two integers
	def multiply(self,x, y):
		return x * y;
	
	#Divide two integers
	def divide(self,x, y):
		return x / y;


			
start = Tk()
obj=calc(start) #object instantiated
start.mainloop()

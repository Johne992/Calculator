#This program makes a simple calculator that can add, subtract, multiply and divide

import math
import Tkinter

class Calculator(object):
	
	def __init__(self):
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

class Engine(object):
	
	def start(self):
		print"\n\n\n"
		print '-'*30
		menu = int(raw_input("\n\nWelcome to Calculator.py!\n\n"))
		print '-'*30
		print"\n\n\n"
		c = Calculator()	
		start()
			
	
begin = Engine()
begin.start()
